# --- APPLICATION WEB INTERACTIVE DES SOLDES SECTORIELS (Version Ultra-Simplifiée) ---

import streamlit as st
import pandas as pd
import plotly.express as px

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(layout="wide", page_title="Carte des Modèles Économiques")

# --- 1. CHARGEMENT ET PRÉPARATION DES DONNÉES ---
@st.cache_data
def load_data():
    excel_file = "donnees_macro_1980-2029_filtrees.xlsx"
    try:
        df = pd.read_excel(excel_file)
        df.columns = df.columns.str.strip()
        df.rename(columns={'Année': 'Year', 'Pays': 'Country', 'SoldeCourant': 'CurrentAccountBalance', 'SoldeBudgétaire': 'BudgetBalance'}, inplace=True)
        # On ne garde que les colonnes strictement nécessaires
        cols_to_keep = ['Year', 'Country', 'CurrentAccountBalance', 'BudgetBalance']
        df = df[cols_to_keep]
        for col in ['CurrentAccountBalance', 'BudgetBalance']:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        df.dropna(subset=['CurrentAccountBalance', 'BudgetBalance', 'Country', 'Year'], inplace=True)
        df['Year'] = df['Year'].astype(int)
        return df
    except FileNotFoundError:
        st.error(f"ERREUR : Le fichier de données '{excel_file}' est introuvable.")
        return pd.DataFrame()

df_all = load_data()

# --- 2. PANNEAU DE CONTRÔLE DANS LA BARRE LATÉRALE ---
st.sidebar.title("Panneau de Contrôle")
annees_disponibles = sorted(df_all['Year'].unique())
annee_debut, annee_fin = st.sidebar.select_slider('Sélectionnez la période :', options=annees_disponibles, value=(2018, 2024))
groupes_de_pays = {
    "Monde Entier": sorted(df_all['Country'].unique()),
    "G7": ['Canada', 'France', 'Germany', 'Italy', 'Japan', 'United Kingdom', 'United States'],
}
groupe_choisi = st.sidebar.selectbox("Choisir un groupe de pays :", options=list(groupes_de_pays.keys()))
pays_selectionnes = st.sidebar.multiselect("Choisir un ou plusieurs pays :", options=groupes_de_pays[groupe_choisi], default=groupes_de_pays[groupe_choisi])

# --- 3. FILTRAGE FINAL DES DONNÉES ---
df_animation = df_all[(df_all['Year'] >= annee_debut) & (df_all['Year'] <= annee_fin) & (df_all['Country'].isin(pays_selectionnes))].copy()
df_animation.sort_values(by=["Year", "Country"], inplace=True)

# --- 4. AFFICHAGE DE L'APPLICATION ---
st.title("Carte Animée des Modèles Économiques Mondiaux")
st.markdown(f"Visualisation de l'évolution de **{len(pays_selectionnes)} pays** sur la période **{annee_debut}-{annee_fin}**.")

if df_animation.empty:
    st.warning("Aucune donnée disponible pour la sélection et la période choisies.")
else:
    fig = px.scatter(
        df_animation, 
        x="CurrentAccountBalance", 
        y="BudgetBalance",
        animation_frame="Year", 
        animation_group="Country",
        hover_name="Country",
        range_x=[-30, 30], 
        range_y=[-30, 30]
    )

    fig.update_layout(
        xaxis_title="Solde de la balance courante (% du PIB)",
        yaxis_title="Solde budgétaire public (% du PIB)",
        title=f"Trajectoire des pays du groupe '{groupe_choisi}'",
        width=800, height=800
    )
    
    fig.add_shape(type="line", x0=-30, y0=-30, x1=30, y1=30, line=dict(color="black", width=2, dash="dash"))
    fig.update_xaxes(zeroline=True, zerolinewidth=2, zerolinecolor='grey')
    fig.update_yaxes(zeroline=True, zerolinewidth=2, zerolinecolor='grey')
    
    st.plotly_chart(fig, use_container_width=True)```

### Explication de la Simplification Radicale

1.  **Imports Supprimés :** `import plotly.graph_objects as go` a été **supprimé**. C'est la source de l'erreur. `numpy` a aussi été retiré car plus nécessaire.
2.  **Fonctionnalités Supprimées :** Pour ne plus dépendre de `plotly.graph_objects`, j ai dû supprimer :
    *   La coloration par niveau de revenu (qui nécessitait le PIB/habitant).
    *   Le dénombrement des pays par quadrant.
    *   La légende personnalisée.
    *   Le contrôle de la vitesse et la fluidité.
3.  **Recentrage sur l'Essentiel :** Ce code ne fait plus qu'une seule chose, mais il devrait la faire sans erreur : **afficher l'animation de base**.

### L'Étape Finale (la dernière)

1.  **Mettez à jour votre fichier `app.py`** sur GitHub avec ce nouveau code simplifié.
2.  **Mettez à jour votre fichier `requirements.txt`** pour qu'il ne contienne que le strict minimum (cela peut aider à éviter les conflits) :
    ```
    streamlit
    pandas
    plotly
    openpyxl
    ```
3.  **Allez sur Streamlit Cloud, supprimez l'application, et redéployez-la.**


Si cette version ultra-simplifiée fonctionne, cela confirmera que le problème vient d'une dépendance complexe de `plotly.graph_objects`. Nous pourrons alors, si vous le souhaitez, réintroduire les fonctionnalités une par une pour voir laquelle cause le conflit. Mais l'objectif premier est d'avoir une application qui se lance.
