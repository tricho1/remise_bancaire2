import streamlit as st
import os

def process_file(input_file):
    # Caractères ASCII à ajouter
    SOH = chr(1)  # Début du fichier
    STX = chr(2)  # Fin du fichier
    
    try:
        # Lecture du fichier uploadé
        content = input_file.getvalue().decode('utf-8')
        
        # Ajout des caractères ASCII
        fichier_modifie = SOH + content + STX
        
        # Création du nom du fichier de sortie
        output_filename = os.path.splitext(input_file.name)[0] + "_modifiee.txt"
        
        return fichier_modifie, output_filename
        
    except Exception as e:
        st.error(f"Une erreur s'est produite : {str(e)}")
        return None, None

def main():
    st.title("Modification de la remise bancaire")
    st.write("Cette application ajoute les caractères ASCII SOH et STX au début et à la fin du fichier.")
    
    # Upload du fichier
    uploaded_file = st.file_uploader("", type=['txt'])
    
    if uploaded_file is not None:
        if st.button("Traiter le fichier"):
            fichier_modifie, output_filename = process_file(uploaded_file)
            
            if fichier_modifie and output_filename:
                # Création du bouton de téléchargement
                st.download_button(
                    label="Télécharger le fichier modifié",
                    data=fichier_modifie.encode('utf-8'),
                    file_name=output_filename,
                    mime="text/plain"
                )
                st.success("Le fichier a été modifié avec succès!")

if __name__ == "__main__":
    main()
