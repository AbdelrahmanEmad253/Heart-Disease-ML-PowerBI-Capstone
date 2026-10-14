"""5-fold CV for prognosis and diagnosis RF models, with/without leakage and duplicates."""
from pathlib import Path
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold, cross_validate

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "datasets"
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
rf = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)

fail = pd.read_csv(DATA / "heart_failure_clinical_records.csv")
heart = pd.read_csv(DATA / "heart.csv")
cases = [
    ("Prognosis", "all features incl. time", fail, "DEATH_EVENT", []),
    ("Prognosis", "without time", fail, "DEATH_EVENT", ["time"]),
    ("Diagnosis", "all features", heart, "target", []),
]
rows = []
for task, feats, df, target, drop in cases:
    for dedup in (False, True):
        # dedup BEFORE splitting so identical rows can never land in train and test
        d = df.drop_duplicates() if dedup else df
        X, y = d.drop(columns=[target] + drop), d[target]
        r = cross_validate(rf, X, y, cv=cv, scoring=["accuracy", "recall", "roc_auc"])
        f = lambda k: f"{r['test_' + k].mean():.3f} ± {r['test_' + k].std():.3f}"
        rows.append(f"| {task} | {feats} | {'yes' if dedup else 'no'} | {len(d)} | "
                    f"{f('accuracy')} | {f('recall')} | {f('roc_auc')} |")

out = ("| Task | Features | Deduplicated | Rows | Accuracy | Recall | ROC-AUC |\n"
       "|---|---|---|---|---|---|---|\n" + "\n".join(rows) + "\n")
print(out)
(ROOT / "outputs" / "cv_results.md").write_text(out, encoding="utf-8")
