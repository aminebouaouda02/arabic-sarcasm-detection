import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

Path("scratch").mkdir(exist_ok=True)
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.sans-serif'] = ['Segoe UI', 'DejaVu Sans', 'Arial']

# 1. Comparaison des modeles
fig, ax = plt.subplots(figsize=(10, 5.5), dpi=200)
models = [
    "UBC-NLP/MARBERTv2 (Fine-Tuning)",
    "AraBERT-twitter (Fine-Tuning)",
    "AraBERT gelé (Moyenne masquée)",
    "AraBERT gelé [CLS] + LR",
    "Multi-tâche AraBERT (lambda=0.5)",
    "Multi-tâche AraBERT (lambda=1.0)",
    "TF-IDF n-grammes caractères",
    "Multi-tâche AraBERT (lambda=0.3)",
    "TF-IDF mots (baseline)",
    "Heuristique Sentiment (CAMeL-Lab)",
    "Zero-shot NLI Français (mDeBERTa)",
    "Zero-shot NLI Arabe (mDeBERTa)",
]
f1_scores = [0.6535, 0.6417, 0.6180, 0.5872, 0.5638, 0.5455, 0.5361, 0.5241, 0.4755, 0.4700, 0.4110, 0.3762]
colors = ['#10b981', '#2563eb', '#3b82f6', '#60a5fa', '#8b5cf6', '#a78bfa', '#f59e0b', '#c084fc', '#94a3b8', '#64748b', '#cbd5e1', '#e2e8f0']

y_pos = np.arange(len(models))
bars = ax.barh(y_pos, f1_scores, color=colors[::-1], height=0.65, edgecolor='none')
ax.set_yticks(y_pos)
ax.set_yticklabels(models[::-1], fontsize=10, fontweight='500', color='#1e293b')
ax.set_xlabel("F1-Score Sarcasme (classe minoritaire)", fontsize=11, fontweight='600', color='#0f172a', labelpad=10)
ax.set_xlim(0, 0.75)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#cbd5e1')
ax.spines['bottom'].set_color('#cbd5e1')
ax.grid(axis='x', linestyle='--', alpha=0.5, color='#e2e8f0')

for bar in bars:
    w = bar.get_width()
    ax.text(w + 0.012, bar.get_y() + bar.get_height()/2, f"{w:.4f}",
            va='center', ha='left', fontsize=9.5, fontweight='bold', color='#1e293b')

plt.title("Classement des Performances F1 - Détection du Sarcasme Arabe", fontsize=14, fontweight='bold', color='#0f172a', pad=15)
plt.tight_layout()
plt.savefig("scratch/chart_models_comparison.png", bbox_inches='tight')
plt.close()

# 2. Prior Shift & Dialectes
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5), dpi=200)

# Prior shift
splits = ['Train (N=11 293)', 'Val (N=1 255)', 'Test Officiel (N=3 000)']
priors = [17.28, 17.29, 27.37]
colors_prior = ['#64748b', '#3b82f6', '#ef4444']
b = ax1.bar(splits, priors, color=colors_prior, width=0.55, edgecolor='#0f172a', linewidth=0.5)
ax1.set_ylabel("Taux de sarcasme (%)", fontsize=10, fontweight='600', color='#1e293b')
ax1.set_ylim(0, 35)
ax1.set_title("Prior Shift Majeur (+10.1 pp)", fontsize=12, fontweight='bold', color='#0f172a')
for bar in b:
    h = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, h + 1, f"{h:.2f}%", ha='center', fontweight='bold', fontsize=10)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

# Dialectes
dialects = ['MSA', 'Egypt', 'Gulf', 'Levant', 'Magreb']
rates = [34.6, 24.8, 21.4, 39.5, 10.9]
b2 = ax2.bar(dialects, rates, color='#0284c7', width=0.55)
ax2.set_ylabel("Taux sarcasme par dialecte (%)", fontsize=10, fontweight='600', color='#1e293b')
ax2.set_ylim(0, 50)
ax2.set_title("Hétérogénéité selon les Dialectes", fontsize=12, fontweight='bold', color='#0f172a')
for bar in b2:
    h = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2, h + 1.2, f"{h:.1f}%", ha='center', fontweight='bold', fontsize=9.5)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig("scratch/chart_prior_shift.png", bbox_inches='tight')
plt.close()

# 3. Multi-tache vs Lambda
fig, ax = plt.subplots(figsize=(7, 4), dpi=200)
lambdas = [0.3, 0.5, 1.0]
f1_mt = [0.5241, 0.5638, 0.5455]
prauc_mt = [0.5162, 0.5833, 0.5259]

ax.plot(lambdas, f1_mt, marker='o', markersize=8, linewidth=2.5, color='#8b5cf6', label='F1 Sarcasme')
ax.plot(lambdas, prauc_mt, marker='s', markersize=8, linewidth=2.5, color='#06b6d4', linestyle='--', label='PR-AUC')
ax.set_xticks(lambdas)
ax.set_xlabel("Poids de la tâche auxiliaire Sentiment (lambda)", fontsize=10, fontweight='600')
ax.set_ylabel("Score de Validation", fontsize=10, fontweight='600')
ax.set_title("Impact de lambda en Multi-Tâche (Optimal à lambda=0.5)", fontsize=12, fontweight='bold', color='#0f172a', pad=12)
ax.set_ylim(0.48, 0.62)
ax.legend(frameon=True, facecolor='white', framealpha=0.9)
ax.scatter([0.5], [0.5638], color='#ef4444', s=120, zorder=5)
ax.annotate("Optimum : F1 = 0.5638\n(équilibre sarcasme/sentiment)", (0.5, 0.5638),
            xytext=(0.52, 0.58), arrowprops=dict(arrowstyle="->", color='#ef4444', lw=1.5),
            fontsize=9.5, fontweight='bold', color='#ef4444')
plt.tight_layout()
plt.savefig("scratch/chart_multitask_lambda.png", bbox_inches='tight')
plt.close()

print("Charts successfully generated.")

