import matplotlib.pyplot as plt
import numpy as np

# --- CONFIGURATION ---
DEEP_GREEN = '#2c867c'
ACID_LIME = '#f3ff8c'

# Standard clean font stack
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Helvetica']
plt.rcParams['text.color'] = DEEP_GREEN
plt.rcParams['axes.labelcolor'] = DEEP_GREEN
plt.rcParams['xtick.color'] = DEEP_GREEN
plt.rcParams['ytick.color'] = DEEP_GREEN

def clean_axes(ax):
    """Creates a clean 'L' frame in Deep Green."""
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(DEEP_GREEN)
    ax.spines['bottom'].set_color(DEEP_GREEN)
    ax.spines['left'].set_linewidth(1.5)
    ax.spines['bottom'].set_linewidth(1.5)

def save_zine_graph(filename):
    plt.savefig(filename, transparent=True, dpi=300, bbox_inches='tight')
    print(f"✅ Saved: {filename}")
    plt.close()

# --- 1. WEEKLY PERFORMANCE ---
days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
scores = [2.37, 2.36, 2.43, 2.34, 2.71, 2.81, 2.68]

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(days, scores, color=ACID_LIME, edgecolor=DEEP_GREEN, linewidth=1.5)

ax.set_ylabel('AVG SCORE', fontweight='bold', labelpad=10)
ax.set_ylim(0, 5)
clean_axes(ax)

for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 0.1, f'{yval}', 
            ha='center', fontweight='bold', size=11)

save_zine_graph('1_weekly_performance.png')

# --- 2. THE LEARNING CURVE ---
months_idx = np.arange(17)
months_labels = ['Oct 24', 'Feb 25', 'Jun 25', 'Oct 25', 'Feb 26']
texture_avg = [2.00, 2.14, 2.50, 2.43, 2.11, 2.00, 2.29, 3.11, 2.50, 2.20, 2.00, 2.83, 2.50, 2.67, 2.60, 3.00, 3.33]

fig, ax = plt.subplots(figsize=(12, 6))
ax.scatter(months_idx, texture_avg, color=DEEP_GREEN, s=100, zorder=3)
z = np.polyfit(months_idx, texture_avg, 1)
p = np.poly1d(z)
ax.plot(months_idx, p(months_idx), color=DEEP_GREEN, linewidth=4, zorder=2)

ax.set_ylabel('TEXTURE RATING', fontweight='bold')
ax.set_xticks([0, 4, 8, 12, 16])
ax.set_xticklabels(months_labels, fontweight='bold')
ax.set_ylim(1, 5)
clean_axes(ax)

save_zine_graph('2_learning_curve.png')

# --- 3. THE VIBE LIFT ---
vibe_labels = ['So-so texture (1-3)', 'Great texture (4-5)']
vibe_scores = [1.83, 3.26]

fig, ax = plt.subplots(figsize=(8, 4))
bars = ax.barh(vibe_labels, vibe_scores, color=[DEEP_GREEN, DEEP_GREEN], edgecolor=DEEP_GREEN)

ax.set_xlabel('VIBE SCORE', fontweight='bold')
ax.set_xlim(0, 5)
clean_axes(ax)

for i, bar in enumerate(bars):
    ax.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height()/2, f'{vibe_scores[i]}', 
            va='center', fontweight='bold', size=12)

save_zine_graph('3_vibe_lift.png')