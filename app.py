import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')
données['ca_produit'] = données['qte']*données['prix']

figure = px.pie(données, values='qte', names='region', title='quantité vendue par région')

figure_2 = px.pie(données, values='qte', names='produit', title='quantité vendue par produit')

figure_3 = px.bar(données, x='produit' , y='ca_produit', title='chiffre affaire par produit')

figure.write_html('ventes-par-region.html')

figure_2.write_html('vente-par-produit.html')

figure_3.write_html('ca-par-produit.html')

print('graphiques générer avec succés ')
