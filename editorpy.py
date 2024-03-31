import streamlit as st
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
import streamlit.components.v1 as components
import io
import sys
import traceback
import matplotlib.pyplot as plt

# Titre de l'application
st.title("Correcteur Syntaxique et Affichage de Plot")

# Zone de texte pour saisir le code Python
code = st.text_area("Saisissez votre code Python ici", height=200)

# Bouton pour exécuter le code et afficher le résultat avec une mise en forme syntaxique
if st.button("Exécuter et afficher le résultat"):
    # Créer un conteneur pour afficher la sortie du code
    output_container = st.empty()

    # Capturer la sortie standard
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()

    # Exécuter le code Python saisi
    try:
        exec(code)
    except Exception as e:
        # Afficher les erreurs s'il y en a
        st.error(f"Erreur lors de l'exécution du code : {e}")
        st.error(traceback.format_exc())

    # Récupérer et afficher la sortie capturée
    output = redirected_output.getvalue()
    formatted_output = f"<pre>{output}</pre>"
    output_container.write(formatted_output)

    # Restaurer la sortie standard
    sys.stdout = old_stdout

    # Mettre en forme le code avec Pygments et l'afficher
    formatted_code = highlight(code, PythonLexer(), HtmlFormatter())
    components.html(formatted_code, height=400)

    # Exécuter le code pour afficher un plot
    try:
        exec(code)
    except Exception as e:
        # Afficher les erreurs s'il y en a
        st.error(f"Erreur lors de l'exécution du code : {e}")
        st.error(traceback.format_exc())
