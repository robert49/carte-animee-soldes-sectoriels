Hugging Face's logo
Hugging Face

Search models, datasets, users...
⌘K
Models
Datasets
Spaces
Buckets
Docs
Enterprise
Pricing


 
Spaces:
Rcauneau
/
carte_soldes_sectoriels


Like
0

Logs
App

Files
Community
Settings
carte_soldes_sectoriels
/
app.py 
Rcauneau's picture
Rcauneau
Upload app.py
ad99edb
VERIFIED
2 days ago

Download

Raw
History
Blame
Edit
Delete

30 kB
# --- APPLICATION WEB INTERACTIVE DES SOLDES SECTORIELS (Version Finale, Complète et Fluide) ---

import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import plotly.graph_objects as go
import numpy as np

# --- DÉBUT DU BLOC MULTILINGUE ---

# Dictionnaire contenant tous les textes de l'application
TEXTS = {
    'fr': {
        'page_title': "Carte des Modèles Économiques",
        'main_title': "Carte Animée des Modèles Économiques Mondiaux",
        'sidebar_title': "Panneau de Contrôle",
        'period_select': "Sélectionner la période :",
        'speed_select': "Choisir la vitesse de l'animation :",
        'forcer_select': "Afficher les noms des pays",
        'group_select': "Choisir un groupe de pays :",
        'country_select': "Choisir un ou plusieurs pays :",
        'show_labels_checkbox': "Afficher les noms des pays",
        'viz_of': "Visualisation de l'évolution de",
        'countries': "pays",
        'over_period': "sur la période",
        'no_data_warning': "Aucune donnée disponible pour la sélection et la période choisies.",
        'xaxis_title': "Solde de la balance courante (% du PIB)",
        'yaxis_title': "Solde budgétaire public (% du PIB)",
        'play_button': "Play",
        'pause_button': "Pause",
        'high_income_group': "Pays à Revenu Élevé",
        'upper_middle_income_group': "Pays à Revenu Intermédiaire Supérieur",
        'lower_middle_income_group': "Pays à Revenu Intermédiaire Inférieur",
        'low_income_group': "Pays à Revenu Faible",
        'high_income_label': 'Revenu élevé',
        'upper_middle_income_label': 'Revenu intermédiaire supérieur',
        'lower_middle_income_label': 'Revenu intermédiaire inférieur',
        'low_income_label': 'Revenu faible',
        'unknown_income_label': 'Inconnu',
        'trajectory_label': "Trajectoire des pays du groupe",
        'Whole_world': "Monde entier",
        'Europe': "Union Européenne",
        'Zone Euro': "Zone Euro",
        'FCFA': "Zone CFA",
        'Slow': "Lente",
        'Normal': "Normale",
        'Fast': "Rapide",
        'Endettement_net': "Zone d'ENDETTEMENT net<br>du secteur privé<br>(S < I)",
        'Epargne_nette': "Zone d'ÉPARGNE nette<br>du secteur privé<br>(S > I)",
        'Def_ext': "<b>Déficit Extérieur</b><br>(X < M)",
        'Exc_ext': "<b>Excédent Extérieur</b><br>(X > M)",
        'Def_budg': "<b>Déficit Budgétaire</b><br>(G > T)",
        'Exc_budg': "<b>Excédent Budgétaire</b><br>(G < T)",
        'Solde_int': "<b>Solde Intérieur Privé</b><br>(S = I)",
        'For_the_year': "<b>Pour l'année",
        'Countries_out_of': "pays sur",
        'In_public_deficit': "en déficit public",
        'En_moyenne': "<b>En moyenne sur la période",
        'des_pays_en_deficit': "des pays en déficit",
        'Animation_realisee': "Animation réalisée par Robert Cauneau, cofondateur de",
        'Panneau_controle': "💡 Utilisez le Panneau de Contrôle pour choisir les pays ou les groupes de pays, pour naviguer dans le temps et pour ajuster la vitesse via le menu latéral. Vous pouvez également forcer l'affichage des noms des pays dans les configurations qui ne l'offrent pas par défaut.",
        'guide_title': "📖 Cliquez ici pour ouvrir le Guide d'Utilisation",
        'guide_content': """        
        ### Guide d'Utilisation de la Carte Animée
Bienvenue sur la Carte Animée des Modèles Économiques Mondiaux. Cet outil interactif vous permet d'explorer les dynamiques des soldes sectoriels pour près de 200 pays de 1980 à 2024.
Pour une analyse approfondie des concepts présentés ici, nous vous invitons à lire l'article complet : **[Le Déficit est la position naturelle du budget de l'Etat](https://mmt-france.org/2025/07/19/le-deficit-est-la-position-naturelle-du-budget-de-letat/)**.
        
#### 1. Comprendre la Carte : Le Décodeur à 4 Quadrants
Ce graphique est une "carte" qui décode la structure économique d'un pays en un seul coup d'œil.
*   **L'axe vertical** représente le **Solde Public**. En bas, l'État est en déficit ; en haut, il est en excédent.
*   **L'axe horizontal** représente le **Solde Extérieur**. À gauche, le pays est en déficit avec le monde ; à droite, il est en excédent.
La position du **Secteur Privé** (ménages et entreprises) se lit par rapport à la **diagonale en pointillés** :
*   **Au-dessus de la diagonale (Zone Orange 🟠) :** Le secteur privé, collectivement, **s'endette**.
*   **En dessous de la diagonale (Zone Verte 🟢) :** Le secteur privé, collectivement, **épargne**.
*La règle d'or : la somme de ces trois soldes est toujours nulle.*
#### 2. Utiliser l'Application : Votre Tableau de Bord
Le **Panneau de Contrôle** situé à gauche vous donne une liberté totale.
*   **Sélectionnez la Période :** Utilisez le **curseur temporel**.
*   **Choisissez la Vitesse :** Utilisez le menu déroulant.
*   **Explorez les Groupes :** Le menu **"Choisir un groupe de pays"** est le meilleur point de départ.
*   **Créez vos Comparaisons :** Utilisez le champ **"Choisir un ou plusieurs pays"** pour des analyses sur mesure.
*   **Affichez les Noms :** Cochez la case **"Afficher les noms des pays"**.
*   **Naviguez dans l'Animation :** Utilisez les boutons **▶️ Play** et **⏸️ Pause** et le **curseur sous le graphique**.
*   **Survolez un point** avec votre souris pour voir le nom du pays.
#### 3. Quelques informations pratiques
*   Les données de certains pays ne sont pas disponibles, notamment pour les premières années, à partir de 1980. Cela se traduit, pour les pays concernés, par une entrée en jeu différée, dans l'hypothèse où l'animation part de 1980.
*   Un clic sur le bouton "clear all" est nécessaire pour vider la liste des pays du monde entier et ainsi permettre le choix individuel d'un ou de plusieurs pays. 
Je vous souhaite une excellente exploration !
        
        
        """, # <--- N'oubliez pas la virgule ici

        
    },

    'en': {
        'page_title': "Map of Economic Models",
        'main_title': "Animated Map of World Economic Models",
        'sidebar_title': "Control Panel",
        'period_select': "Select the period:",
        'speed_select': "Choose the animation speed:",
        'forcer_select': "Show country names",
        'group_select': "Choose a group of countries:",
        'country_select': "Choose one or more countries:",
        'show_labels_checkbox': "Show country names",
        'viz_of': "Visualizing the evolution of",
        'countries': "countries",
        'over_period': "over the period",
        'no_data_warning': "No data available for the selected period and countries.",
        'xaxis_title': "Current Account Balance (% of GDP)",
        'yaxis_title': "Government Budget Balance (% of GDP)",
        'play_button': "Play",
        'pause_button': "Pause",
        'high_income_group': "High Income Countries",
        'upper_middle_income_group': "Upper-Middle Income Countries",
        'lower_middle_income_group': "Lower-Middle Income Countries",
        'low_income_group': "Low Income Countries",
        'high_income_label': 'High Income',
        'upper_middle_income_label': 'Upper middle Income',
        'lower_middle_income_label': 'Lower middle Income',
        'low_income_label': 'Low Income',
        'unknown_income_label': 'Unknown',
        'trajectory_label': "Trajectory of the group's countries",
        'Whole_world': "Whole world",
        'Europe': "European Union",
        'Zone Euro': "Euro Area",
        'FCFA': "CFA Zone",
        'Slow': "Slow",
        'Normal': "Normal",
        'Fast': "Fast",
        'Endettement_net': "Net Debt Area<br>of the private sector<br>(S < I)",
        'Epargne_nette': "Net Savings Area<br>of the private sector<br>(S > I)",
        'Def_ext': "<b>External Deficit</b><br>(X < M)",
        'Exc_ext': "<b>External Surplus</b><br>(X > M)",
        'Def_budg': "<b>Budget deficit</b><br>(G > T)",
        'Exc_budg': "<b>Budget Surplus</b><br>(G < T)",
        'Solde_int': "<b>Private Internal Balance</b><br>(S = I)",        
        'For_the_year': "<b>For the year",
        'Countries_out_of': "countries out of",
        'In_public_deficit': "in public deficit",
        'En_moyenne': "<b>On average over the period",
        'des_pays_en_deficit': "of countries in deficit",
        'Animation_realisee': "Animation produced by Robert Cauneau, co-founder of",
        'Panneau_controle': "💡 Use the Control Panel to choose countries or groups of countries, to navigate through time, and to adjust the speed via the side menu. You can also force the display of country names in configurations that do not offer it by default.",
        'guide_title': "📖 Click here to open the User Guide",
        'guide_content': """        
        ### Animated Map User Guide
Welcome to the Animated Map of Global Economic Models. This interactive tool allows you to explore the dynamics of sectoral balances for nearly 200 countries from 1980 to 2024.
For an in-depth analysis of the concepts presented here, we invite you to read the full article: **[The Deficit is the natural position of the state budget](https://mmt-france.org/2025/07/19/the-deficit-is-the-natural-position-of-the-state-budget/)**.
#### 1. Understanding the Map: The 4-Quadrant Decoder
This graph is a "map" that decodes a country's economic structure at a glance.
* **The vertical axis** represents the **Public Balance**. At the bottom, the government is in deficit; at the top, it is in surplus.
* **The horizontal axis** represents the **External Balance**. On the left, the country is in deficit with the world; on the right, it is in surplus.
The position of the **Private Sector** (households and businesses) is read in relation to the **dotted diagonal**:
* **Above the diagonal (Orange Zone 🟠):** The private sector, collectively, **is in debt**.
* **Below the diagonal (Green Zone 🟢):** The private sector, collectively, **saves**.
*The golden rule: the sum of these three balances is always zero.*
#### 2. Using the App: Your Dashboard
The **Control Panel** on the left gives you complete freedom.
* **Select the Period:** Use the **time slider**.
* **Choose the Speed:** Use the drop-down menu. * **Explore the Groups:** The **"Choose a country group"** menu is the best starting point.
* **Create your Comparisons:** Use the **"Choose one or more countries"** field for customized analyses.
* **Display Names:** Check the **"Display country names"** box.
* **Navigate the Animation:** Use the **▶️ Play** and **⏸️ Pause** buttons and the **slider below the graph**.
* **Hover your mouse over a point** to see the country name.
#### 3. Some practical information
*  Data for some countries are not available, particularly for the early years, starting in 1980. This results in a delayed start for the countries concerned, assuming the data begins in 1980.
*  Clicking the "clear all" button is required to clear the list of countries worldwide and thus allow you to individually select one or more countries.
I hope you enjoy exploring!
        """, # <--- N'oubliez pas la virgule ici


    }
}

options_langue = ["🇫🇷 Français", "🇬🇧 English"]


lang_selectionnee = st.sidebar.radio(
    "Sélecteur de langue", # Un label descriptif mais qui sera caché
    options_langue, 
    index=0, 
    key="lang_selector",
    label_visibility="collapsed" # Cache le label "Sélecteur de langue"
)

# On détermine le code de la langue de manière infaillible
if lang_selectionnee == options_langue[0]: # Si c'est le premier élément ("🇫🇷 Français")
    lang_code = 'fr'
else: # Sinon, c'est le second
    lang_code = 'en'

# 3. On définit la variable 'T' une bonne fois pour toutes
T = TEXTS[lang_code]

# --- CONFIGURATION DE LA PAGE ---

st.set_page_config(layout="wide", page_title=T['page_title'])

# --- MESURE ANONYME DE LA FRÉQUENTATION ---
# Une consultation est envoyée une seule fois par session Streamlit.
# GoatCounter fonctionne sans cookie ni identifiant personnel persistant.
if "goatcounter_pageview_sent" not in st.session_state:
    components.html(
        """
        <script
            data-goatcounter="https://rcauneau.goatcounter.com/count"
            data-goatcounter-settings='{
                "allow_frame": true,
                "path": "/carte-soldes-sectoriels",
                "title": "Carte animée des soldes sectoriels"
            }'
            async
            src="https://gc.zgo.at/count.js">
        </script>
        """,
        height=0,
    )
    st.session_state["goatcounter_pageview_sent"] = True

# --- 1. CHARGEMENT ET PRÉPARATION DES DONNÉES ---
@st.cache_data
def load_data():
    excel_file = "data.xlsx"
    try:
        df = pd.read_excel(excel_file, engine='openpyxl')
        df.columns = df.columns.str.strip()
        df.rename(columns={'Année': 'Year', 'Pays': 'Country', 'SoldeCourant': 'CurrentAccountBalance', 'SoldeBudgétaire': 'BudgetBalance'}, inplace=True)
        for col in ['CurrentAccountBalance', 'BudgetBalance', 'PIB/habitant']:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        df.dropna(subset=['CurrentAccountBalance', 'BudgetBalance', 'Country', 'Year'], inplace=True)
        df['Year'] = df['Year'].astype(int)
        return df
    except FileNotFoundError:
        st.error(f"ERREUR : Le fichier de données '{excel_file}' est introuvable.")
        return pd.DataFrame()

def classifier_revenu(pib_par_habitant):
    if pd.isna(pib_par_habitant): return T['unknown_income_label']
    if pib_par_habitant <= 1135: return T['low_income_label']
    elif pib_par_habitant <= 4465: return T['lower_middle_income_label']
    elif pib_par_habitant <= 13845: return T['upper_middle_income_label']
    else: return T['high_income_label']

df_all = load_data()
if not df_all.empty:
    df_latest_pib = df_all.sort_values('Year').drop_duplicates('Country', keep='last')
    country_to_income = df_latest_pib.set_index('Country')['PIB/habitant'].apply(classifier_revenu).to_dict()
    df_all['Niveau_Revenu'] = df_all['Country'].map(country_to_income)


    

st.sidebar.title(T['sidebar_title'])
annees_disponibles = sorted(df_all['Year'].unique())


annee_debut, annee_fin = st.sidebar.select_slider(T['period_select'], options=annees_disponibles, value=(1980, 2024))
vitesses = {T['Slow']: 800, T['Normal']: 400, T['Fast']: 150}
vitesse_choisie = st.sidebar.selectbox(T['speed_select'], options=list(vitesses.keys()), index=1)
duree_frame = vitesses[vitesse_choisie]

#st.sidebar.markdown("---") # Ajoute une ligne de séparation
forcer_labels = st.sidebar.checkbox(T['forcer_select'], value=False)

        

# --- DÉBUT DE LA MODIFICATION ---
# On crée d'abord des listes de pays pour chaque catégorie de revenu
pays_revenu_eleve = sorted(df_all[df_all['Niveau_Revenu'] == T['high_income_label']]['Country'].unique())
pays_revenu_intermediaire_sup = sorted(df_all[df_all['Niveau_Revenu'] == T['upper_middle_income_label']]['Country'].unique())
pays_revenu_intermediaire_inf = sorted(df_all[df_all['Niveau_Revenu'] == T['lower_middle_income_label']]['Country'].unique())
pays_revenu_faible = sorted(df_all[df_all['Niveau_Revenu'] == T['low_income_label']]['Country'].unique())

groupes_de_pays = {
    T['Whole_world']: sorted(df_all['Country'].unique()),
    T['Europe']: ['Austria', 'Belgium', 'Bulgaria', 'Croatia', 'Cyprus', 'Czechia', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Ireland', 'Italy', 'Latvia', 'Lithuania', 'Luxembourg', 'Malta', 'Netherlands', 'Poland', 'Portugal', 'Romania', 'Slovakia', 'Slovenia', 'Spain', 'Sweden'],
    T['Zone Euro']: ['Austria', 'Belgium', 'Croatia', 'Cyprus', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Ireland', 'Italy', 'Latvia', 'Lithuania', 'Luxembourg', 'Malta', 'Netherlands', 'Portugal', 'Slovakia', 'Slovenia', 'Spain'],
    T['FCFA']: ['Benin', 'Burkina Faso', "Cote d'Ivoire", 'Guinea-Bissau', 'Mali', 'Niger', 'Senegal', 'Togo', 'Cameroon', 'Central African Republic', 'Chad', 'Congo, Republic of', 'Equatorial Guinea', 'Gabon', 'Comoros'],
    "G20": ['Argentina', 'Australia', 'Brazil', 'Canada', 'China', 'France', 'Germany', 'India', 'Indonesia', 'Italy', 'Japan', 'Korea, Rep.', 'Mexico', 'Russia', 'Saudi Arabia', 'South Africa', 'Turkey', 'UK', 'USA'],
    "G7": ['Canada', 'France', 'Germany', 'Italy', 'Japan', 'UK', 'USA'],
    "BRICS+": ['Brazil', 'Russia', 'India', 'China', 'South Africa', 'Saudi Arabia', 'Egypt', 'Ethiopia', 'Iran, Islamic Rep. of', 'United Arab Emirates'],
    # On ajoute les nouvelles catégories au dictionnaire
    T['high_income_group']: pays_revenu_eleve,
    T['upper_middle_income_group']: pays_revenu_intermediaire_sup,
    T['lower_middle_income_group']: pays_revenu_intermediaire_inf,
    T['low_income_group']: pays_revenu_faible,
}
# --- FIN DE LA MODIFICATION ---


groupe_choisi = st.sidebar.selectbox(T['group_select'], options=list(groupes_de_pays.keys()))
pays_selectionnes = st.sidebar.multiselect(T['country_select'], options=groupes_de_pays[groupe_choisi], default=groupes_de_pays[groupe_choisi])

# --- 3. FILTRAGE ET PRÉPARATION DES DONNÉES ---
df_animation = df_all[(df_all['Year'] >= annee_debut) & (df_all['Year'] <= annee_fin) & (df_all['Country'].isin(pays_selectionnes))].copy()
df_animation.sort_values(by="Year", inplace=True)

# --- 4. AFFICHAGE DE L'APPLICATION ---
st.title(T['main_title'])

with st.expander(T['guide_title']):
    st.markdown(T['guide_content'], unsafe_allow_html=True)

st.markdown(f"{T['viz_of']} **{len(pays_selectionnes)}** {T['countries']} {T['over_period']} **{annee_debut}-{annee_fin}**.")

if df_animation.empty:
    st.warning(T['no_data_warning'])
else:
    range_xy = [-30, 30]
    years_sorted = sorted(df_animation['Year'].unique())

    show_labels = (len(pays_selectionnes) <= 20) or forcer_labels
  
    color_map = {'Revenu élevé': 'darkblue', 'Revenu intermédiaire supérieur': 'green',
                 'Revenu intermédiaire inférieur': 'orange', 'Revenu faible': 'brown', 'Inconnu': 'grey'}

    fig = go.Figure()

    # --- DÉBUT DU BLOC À AJOUTER : PRÉ-CALCUL DE LA MOYENNE ---
    # On calcule le nombre moyen de pays en déficit sur toute la période
    pays_en_deficit_par_an = df_animation[df_animation['BudgetBalance'] < 0].groupby('Year')['Country'].count()
    total_pays_par_an = df_animation.groupby('Year')['Country'].count()
    
    # On s'assure de ne pas diviser par zéro si une année n'a pas de pays
    pourcentage_par_an = (pays_en_deficit_par_an.reindex(total_pays_par_an.index, fill_value=0) / total_pays_par_an * 100)
    pourcentage_moyen_deficit = pourcentage_par_an.mean()
    # --- FIN DU BLOC À AJOUTER ---

    frames = []
    for year in years_sorted:
        df_year = df_animation[df_animation['Year'] == year]
        count_hd = len(df_year[(df_year['BudgetBalance'] >= 0) & (df_year['CurrentAccountBalance'] >= 0)])
        count_hg = len(df_year[(df_year['BudgetBalance'] >= 0) & (df_year['CurrentAccountBalance'] < 0)])
        count_bg = len(df_year[(df_year['BudgetBalance'] < 0) & (df_year['CurrentAccountBalance'] < 0)])
        count_bd = len(df_year[(df_year['BudgetBalance'] < 0) & (df_year['CurrentAccountBalance'] >= 0)])
        total_deficit = count_bg + count_bd
        total_pays = len(df_year)
        
        annotations = [
            go.layout.Annotation(x=0.745, y=0.97, xref='paper', yref='paper', text=f"N={count_hd}", showarrow=False, align='right', font=dict(size=14, color='black')),
            go.layout.Annotation(x=0.23, y=0.97, xref='paper', yref='paper', text=f"N={count_hg}", showarrow=False, align='left', font=dict(size=14, color='black')),
            go.layout.Annotation(x=0.23, y=0.04, xref='paper', yref='paper', text=f"N={count_bg}", showarrow=False, align='left', font=dict(size=14, color='black')),
            go.layout.Annotation(x=0.745, y=0.04, xref='paper', yref='paper', text=f"N={count_bd}", showarrow=False, align='right', font=dict(size=14, color='black')),
        ]
        if total_pays > 0:

            # annotations.append(go.layout.Annotation(x=0.5, y=-0.16, xref='paper', yref='paper', text=f"Animation réalisée par Robert Cauneau, cofondateur de <a href="https://mmt-france.org/">MMT-France</a> (source : IMF WEO)", showarrow=False, font=dict(size=16, color='black')))
            credit_text = f"{T['Animation_realisee']} <a href='https://mmt-france.org/'>MMT-France</a> (source: IMF WEO)"

            annotations.append(go.layout.Annotation(
                x=0.5, y=-0.18, xref='paper', yref='paper', 
                text=credit_text, 
                showarrow=False, 
                font=dict(size=16, color='black')
            ))
            
            pourcentage_annee = (total_deficit / total_pays) * 100
    
            # Ligne 1 : Les chiffres pour l'année en cours


            annotations.append(go.layout.Annotation(
                x=0.5, y=0.07, xref='paper', yref='paper',
                #text=f"T['For_the_year'] {year}</b> : {total_deficit} T['Countries_out_of'] {total_pays} T['In_public_deficit'] ({pourcentage_annee:.1f}%)",
                text=f"{T['For_the_year']} {year}</b>: {total_deficit} {T['Countries_out_of']} {total_pays} {T['In_public_deficit']} ({pourcentage_annee:.1f}%)",
                showarrow=False, font=dict(size=14, color='black')
            ))
    
            # Ligne 2 : La moyenne sur la période


            annotations.append(go.layout.Annotation(
                x=0.5, y=0.035, xref='paper', yref='paper',
                text=f"{T['En_moyenne']} {annee_debut}-{annee_fin}</b>: {pourcentage_moyen_deficit:.1f}% {T['des_pays_en_deficit']}",
                showarrow=False, font=dict(size=14, color='black')
            ))
        # --- FIN DU BLOC MODIFIÉ ---

        text_labels_bold = [f'<b>{country}</b>' for country in df_year['Country']]

        frames.append(go.Frame(
            data=[go.Scatter(
                x=df_year['CurrentAccountBalance'], y=df_year['BudgetBalance'],
                mode='markers+text' if show_labels else 'markers',
                text=text_labels_bold, # On utilise la nouvelle liste de textes
                textposition='top center',
                # On peut définir plus de styles pour la police si on le souhaite
                textfont={'size':10, 'color':'black', 'family':'Arial, sans-serif'},
                hoverinfo='text', 
                hovertext=df_year['Country'], # Le survol reste le nom simple
                marker={'size': 7, 'color': df_year['Niveau_Revenu'].map(color_map)}
            )],
            name=str(year),
            layout=go.Layout(annotations=annotations)
        ))
    
    if frames:
        fig.add_trace(frames[0].data[0])
        fig.update_layout(annotations=frames[0].layout.annotations)
        fig.frames = frames

        # --- DÉBUT DE LA SECTION CORRIGÉE ---
        # Configuration des contrôles d'animation avec la vitesse variable
        fig.update_layout(
            updatemenus=[dict(
                type="buttons",
                showactive=False,
                direction="left", # Aligne les boutons horizontalement
                y=-0.25,          # Position verticale, alignée avec le slider
                x=0,              # Commence au bord gauche
                xanchor="left",
                yanchor="top",
                pad={"r": 10, "t": 0}, # Ajoute un peu d'espace à droite des boutons
                buttons=[dict(
                    label="▶️", # Icône Play
                    method="animate", 
                    args=[None, {"frame": {"duration": duree_frame, "redraw": True}, 
                                "fromcurrent": True, 
                                "transition": {"duration": duree_frame * 0.8}}]
                ), dict(
                    label="⏸️", # Icône Pause
                    method="animate", 
                    args=[[None], {"frame": {"duration": 0, "redraw": False}, "mode": "immediate", "transition": {"duration": 0}}]
                )]
            )],
            sliders=[dict(
                active=0, 
                y=-0.15, 
                x=0.1, # On décale le slider pour laisser la place aux 2 boutons
                xanchor="left", 
                yanchor="top", 
                len=0.9, # On ajuste la longueur du slider
                transition={"duration": duree_frame * 0.8},
                steps=[dict(
                    method="animate", 
                    args=[[f.name], {"frame": {"duration": 300, "redraw": True}, "mode": "immediate"}], 
                    label=f.name
                ) for f in fig.frames]
            )]
        )
    
    
    
# Dictionnaires de seuils et de couleurs
        seuils_revenu_texte_titre = {
            T['high_income_group']: '(GDP/hab ≥ 13 846 \\$)',
            T['upper_middle_income_group']: '(GDP/hab : 4 466 \\$ – 13 845 \\$)',
            T['lower_middle_income_group']: '(GDP/hab : \\1 136 $ – 4 465 \\$)',
            T['low_income_group']: '(GDP/hab ≤ \\1 135 $)'
        }
        # On fait correspondre les noms longs des groupes aux noms courts du color_map
        group_to_color_key = {
            T['high_income_group']: 'Revenu élevé',
            T['upper_middle_income_group']: 'Revenu intermédiaire supérieur',
            T['lower_middle_income_group']: 'Revenu intermédiaire inférieur',
            T['low_income_group']: 'Revenu faible'
        }

        # On construit le titre du graphique
        #titre_principal = f"T['trajectory_label'] '{groupe_choisi}'"
        titre_principal = f"{T['trajectory_label']} '{groupe_choisi}'"

        # On récupère la couleur. Par défaut, 'black'
        couleur_titre = color_map.get(group_to_color_key.get(groupe_choisi), 'black')

        # On vérifie si le groupe choisi est une catégorie de revenu
        if groupe_choisi in seuils_revenu_texte_titre:
            # Si oui, on ajoute le seuil en dollars
            titre_principal += f" {seuils_revenu_texte_titre[groupe_choisi]}"

        # On applique toute la mise en page en une seule fois
        fig.update_layout(
            xaxis=dict(range=range_xy, zeroline=True, zerolinewidth=2, zerolinecolor='grey'),
            yaxis=dict(
                range=range_xy, 
                zeroline=True, 
                zerolinewidth=2, 
                zerolinecolor='grey',
                scaleanchor="x", # <-- LIGNE AJOUTÉE ICI
                scaleratio=1,    # <-- On s'assure que le ratio est de 1 pour 1
            ),
           
            xaxis_title=dict(text=f"<b>{T['xaxis_title']}</b>", font=dict(size=16, color="black")),
            yaxis_title=dict(text=f"<b>{T['yaxis_title']}</b>", font=dict(size=16, color="black")),
            title=dict(text=titre_principal, font=dict(color=couleur_titre)),
            width=800,
            height=800,
            showlegend=False,            
        )

        # On ajoute les textes des zones (inchangé)
        fig.add_annotation(
            x=19, y=-19, text=T['Epargne_nette'],
            showarrow=False, font=dict(color="darkgreen", size=12), textangle=-45
        )
       
        fig.add_annotation(    
            x=-19, y=19, text=T['Endettement_net'],
            showarrow=False, font=dict(color="darkred", size=12), textangle=-45
        
   )    

        # --- AJOUT DES MENTIONS DE BILL MITCHELL ---

      
        fig.add_annotation(
            x=0, y=30, # Positionné au centre horizontalement, tout en haut
            yanchor="bottom",
            text=T['Exc_budg'],
            showarrow=False, font=dict(size=12, color="black")
        )

        # Mention "Déficit Budgétaire" en bas
        fig.add_annotation(
            x=0, y=-30, # Positionné au centre horizontalement, tout en bas
            yanchor="top",
            text=T['Def_budg'],
            showarrow=False, font=dict(size=12, color="black")
        )

        
        # Mention "Déficit" Extérieur à gauche (vertical)
        fig.add_annotation(
            x=-30, y=-5,
            xanchor="center", # On ancre au centre
            yanchor="bottom", # On ancre par le bas
            text=T['Def_ext'],
            textangle=-90, # <-- Rotation de -90 degrés
            showarrow=False, font=dict(size=12, color="black")
        )

        # Mention "Excédent Extérieur" à droite (vertical)
        fig.add_annotation(
            x=30, y=5,
            xanchor="center", # On ancre au centre
            yanchor="top",    # On ancre par le haut
            text=T['Exc_ext'],
            textangle=270, # <-- Rotation de +90 degrés
            showarrow=False, font=dict(size=12, color="black")
        )

        # Mention "Private Domestic Balance" dans l'angle haut-droit
        fig.add_annotation(
            x=40, y=30, # Positionné exactement dans le coin
            xanchor="right",
            yanchor="bottom",
            text=T['Solde_int'],
            showarrow=False,
            font=dict(size=12, color="black")
        )
        # --- FIN DU BLOC CORRIGÉ ---

        
        fig.add_shape(type="line", x0=range_xy[0], y0=range_xy[0], x1=range_xy[1], y1=range_xy[1], line=dict(color="black", width=2, dash="dash"))
        fig.add_shape(type="path", path=f" M {range_xy[0]}, {range_xy[0]} L {range_xy[1]}, {range_xy[0]} L {range_xy[1]}, {range_xy[1]} Z", fillcolor="green", opacity=0.08, layer="below", line_width=0)
        fig.add_shape(type="path", path=f" M {range_xy[0]}, {range_xy[0]} L {range_xy[0]}, {range_xy[1]} L {range_xy[1]}, {range_xy[1]} Z", fillcolor="red", opacity=0.08, layer="below", line_width=0)
        
        st.plotly_chart(fig, use_container_width=True)
        st.info(T['Panneau_controle'])
    else:
        st.warning("Aucune donnée d'animation n'a pu être générée.")

