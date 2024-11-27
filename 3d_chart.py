
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Dati per il grafico
years = np.array([0, 1, 2, 3, 4])  # Anni (asse X)
gamification_productivity = np.array([100, 115, 140, 150, 155])  # Produttività (asse Y) per "Gamification"
standard_productivity = np.array([100, 102.5, 105, 107.5, 110])  # Produttività (asse Y) per "Standard"
companies = np.array([0, 1])  # Gamification = 0, Standard = 1 (asse Z)

# Creazione del grafico 3D
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Linea per "Gamification"
ax.plot(
    years, 
    gamification_productivity, 
    zs=0, 
    zdir='z', 
    label='Gamification', 
    linewidth=3, 
    color='#FF6F91'
)

# Linea per "Standard"
ax.plot(
    years, 
    standard_productivity, 
    zs=1, 
    zdir='z', 
    label='Standard', 
    linewidth=3, 
    color='#6B7280'
)

# Etichette degli assi
ax.set_xlabel('Years', labelpad=15, fontsize=12)
ax.set_ylabel('Productivity (%)', labelpad=15, fontsize=12)
ax.set_zlabel('Company', labelpad=15, fontsize=12)

# Etichette per l'asse Z
ax.set_zticks([0, 1])
ax.set_zticklabels(['Gamification', 'Standard'])

# Titolo
ax.set_title(
    'Gamification vs Standard Productivity', 
    fontsize=16, 
    pad=30, 
    color='black'
)

# Personalizzazione degli assi
ax.tick_params(axis='x', labelsize=10)
ax.tick_params(axis='y', labelsize=10)
ax.tick_params(axis='z', labelsize=10)

# Aggiunta di griglia e legenda
ax.grid(color='gray', linestyle='--', linewidth=0.5)
ax.legend(loc='upper left', fontsize=10)

# Salva il grafico come immagine
plt.savefig('3d_productivity_chart.png', dpi=300, bbox_inches='tight')

# Mostra il grafico
plt.show()
