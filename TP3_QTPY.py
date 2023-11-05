import sys
from PyQt6.QtWidgets import *

from db_methodes import *

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()  # fait l'aapel sur la methode initUI()
        
    def initUI(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.setWindowTitle("Application de gestion d'emploi de temps")
        self.setGeometry(100, 100, 700, 450)
        
        self.tab_widget = QTabWidget()
        self.layout.addWidget(self.tab_widget)
        
        self.home_tab = QWidget()
        self.tab_widget.addTab(self.home_tab, "Home")
        
        self.utilisateurs_tab = QWidget()
        self.tab_widget.addTab(self.utilisateurs_tab, "Gestion d'utilisateurs")
        
        self.cours_tab = QWidget()
        self.tab_widget.addTab(self.cours_tab, "Gestion de Cours")
        
        self.salles_tab = QWidget()
        self.tab_widget.addTab(self.salles_tab, "Gestion de Salles")
        
        self.emploi_tab = QWidget()
        self.tab_widget.addTab(self.emploi_tab, "Gestion d'emploi de temps")
        self.tab_widget.currentChanged.connect(self.loadTabContent)
    
    def loadTabContent(self, index):
        # Définir le contenu de chaque onglet en fonction de son index
        if index == 0:
            self.home()
        elif index == 1:
            self.utilisateurs()
        elif index == 2:
            self.cours()
        elif index == 3:
            self.salle()
        elif index == 4:
            self.emploi()

        

        
    # pour clear frame 
    def clear_frame(self, frame):
        for widget in frame.findChildren(QWidget):
            widget.deleteLater()
            
    def add_utilisateur(self):
        self.clear_frame(self.utilisateurs_tab)
        form_frame = QWidget()
        form_layout = QFormLayout()
        form_frame.setLayout(form_layout)
        self.utilisateurs_tab.layout().addWidget(form_frame)
        
        frame_title = QLabel("Ajout d'utilisateurs")
        frame_title.setFont(self.font())
        form_layout.addRow(frame_title)
        
        id_label = QLabel("Id:")
        self.id_entry = QLineEdit()
        form_layout.addRow(id_label, self.id_entry)
        
        nom_label = QLabel("Nom:")
        self.nom_entry = QLineEdit()
        form_layout.addRow(nom_label, self.nom_entry)
        
        prenom_label = QLabel("Prénom:")
        self.prenom_entry = QLineEdit()
        form_layout.addRow(prenom_label, self.prenom_entry)
        
        role_label = QLabel("Rôle:")
        self.role_entry = QLineEdit()
        form_layout.addRow(role_label, self.role_entry)
        
        email_label = QLabel("Email:")
        self.email_entry = QLineEdit()
        form_layout.addRow(email_label, self.email_entry)
        
        button_submit = QPushButton("Ajouter")
        button_submit.clicked.connect(self.submit_form)
        form_layout.addWidget(button_submit)

    def submit_form(self):
        id = self.id_entry.text()
        nom = self.nom_entry.text()
        prenom = self.prenom_entry.text()
        role = self.role_entry.text()
        email = self.email_entry.text()
        create_utilisateur(id, nom, prenom, role, email)
        self.clear_frame(self.utilisateurs_tab)
        self.utilisateurs()

    def display_utilisateurs(self):
        self.clear_frame(self.utilisateurs_tab)
        utilisateurs = get_all_utilisateurs()

        table = QTreeWidget()
        table.setHeaderLabels(["ID", "Nom", "Prénom", "Rôle", "Email"])
        self.utilisateurs_tab.layout().addWidget(table)

        for utilisateur in utilisateurs:
            item = QTreeWidgetItem(table)
            item.setText(0, str(utilisateur[0]))  # Convert ID to a string
            item.setText(1, utilisateur[1])
            item.setText(2, utilisateur[2])
            item.setText(3, utilisateur[3])
            item.setText(4, utilisateur[4])

        home_btn = QPushButton("Retour")
        home_btn.clicked.connect(self.utilisateurs)  # Connect to the method
        self.utilisateurs_tab.layout().addWidget(home_btn)




    def update_utilisateur(self):
        self.clear_frame(self.utilisateurs_tab)
        form_frame = QWidget()
        form_layout = QFormLayout()
        form_frame.setLayout(form_layout)
        self.utilisateurs_tab.layout().addWidget(form_frame)

        frame_title = QLabel("Update d'utilisateurs")
        frame_title.setFont(self.font())
        form_layout.addRow(frame_title)

        id_label = QLabel("Id:")
        self.id_entry = QLineEdit()
        form_layout.addRow(id_label, self.id_entry)

        nom_label = QLabel("Nom:")
        self.nom_entry = QLineEdit()
        form_layout.addRow(nom_label, self.nom_entry)

        prenom_label = QLabel("Prénom:")
        self.prenom_entry = QLineEdit()
        form_layout.addRow(prenom_label, self.prenom_entry)

        role_label = QLabel("Rôle:")
        self.role_entry = QLineEdit()
        form_layout.addRow(role_label, self.role_entry)

        email_label = QLabel("Email:")
        self.email_entry = QLineEdit()
        form_layout.addRow(email_label, self.email_entry)

        button_submit = QPushButton("Update")
        button_submit.clicked.connect(self.submit_update)
        form_layout.addWidget(button_submit)

    def submit_update(self):
        id = self.id_entry.text()
        nom = self.nom_entry.text()
        prenom = self.prenom_entry.text()
        role = self.role_entry.text()
        email = self.email_entry.text()
        result = update_utilisateur(id, nom, prenom, role, email)

        if result == 0:
            print("Utilisateur introuvable, mise à jour non effectuée")
        else:
            self.clear_frame(self.utilisateurs_tab)
            self.utilisateurs()

    def delete_utilisateur(self):
        self.clear_frame(self.utilisateurs_tab)
        form_frame = QWidget()
        form_layout = QFormLayout()
        form_frame.setLayout(form_layout)
        self.utilisateurs_tab.layout().addWidget(form_frame)

        frame_title = QLabel("Delete d'utilisateurs")
        frame_title.setFont(self.font())
        form_layout.addRow(frame_title)

        id_label = QLabel("Id:")
        self.id_entry = QLineEdit()
        form_layout.addRow(id_label, self.id_entry)

        button_submit = QPushButton("Delete")
        button_submit.clicked.connect(self.submit_delete)
        form_layout.addWidget(button_submit)

    def submit_delete(self):
        id = self.id_entry.text()
        delete_utilisateur(id)
        self.clear_frame(self.utilisateurs_tab)
        self.utilisateurs()

    def utilisateurs(self):
        existing_layout = self.utilisateurs_tab.layout()
        if existing_layout:
            QWidget().setLayout(existing_layout)
        self.tab_widget.setCurrentIndex(1)
        form_layout = QVBoxLayout()  
        self.utilisateurs_tab.setLayout(form_layout)  
        
        frame_title = QLabel("Gestion d'utilisateurs :")
        font = frame_title.font()
        font.setBold(True)  
        frame_title.setFont(font)
        frame_title.setStyleSheet("color: blue;")  
        form_layout.addWidget(frame_title)
        
        list_button = QPushButton("Liste des Utilisateurs")
        list_button.clicked.connect(self.display_utilisateurs)
        form_layout.addWidget(list_button)

        add_button = QPushButton("ajouter Utilisateur")
        add_button.clicked.connect(self.add_utilisateur)
        form_layout.addWidget(add_button)

        edit_button = QPushButton("editer Utilisateur")
        edit_button.clicked.connect(self.update_utilisateur)
        form_layout.addWidget(edit_button)

        delete_button = QPushButton("supprimer Utilisateurs")
        delete_button.clicked.connect(self.delete_utilisateur)
        form_layout.addWidget(delete_button)
        

    def home(self):
        existing_layout = self.utilisateurs_tab.layout()
        if existing_layout:
            QWidget().setLayout(existing_layout)
        self.tab_widget.setCurrentIndex(0)

    def cours(self):
        existing_layout = self.cours_tab.layout()
        if existing_layout:
            QWidget().setLayout(existing_layout)  # Clear the existing layout
        self.tab_widget.setCurrentIndex(2)
        form_layout = QVBoxLayout()  
        self.cours_tab.setLayout(form_layout)
        
        frame_title = QLabel("Gestion des Cours:")
        font = frame_title.font()
        font.setBold(True)
        frame_title.setFont(font)
        frame_title.setStyleSheet("color: blue;")
        form_layout.addWidget(frame_title)
    
        list_button = QPushButton("Liste des cours")
        list_button.clicked.connect(self.display_cours)
        form_layout.addWidget(list_button)
    
        add_button = QPushButton("ajouter cours")
        add_button.clicked.connect(self.add_cours)
        form_layout.addWidget(add_button)
    
        edit_button = QPushButton("editer cours")
        edit_button.clicked.connect(self.update_cours)
        form_layout.addWidget(edit_button)
    
        delete_button = QPushButton("supprimer cours")
        delete_button.clicked.connect(self.delete_cours)
        form_layout.addWidget(delete_button)


    def display_cours(self):
        self.clear_frame(self.cours_tab)
        cours = get_all_cours()

        table = QTreeWidget()
        table.setHeaderLabels(["ID", "Nom", "Description"])
        self.cours_tab.layout().addWidget(table)
        for cour in cours:
            item = QTreeWidgetItem(table)
            item.setText(0, str(cour[0]))  # Convert the integer to a string
            item.setText(1, cour[1])
            item.setText(2, cour[2])

        home_btn = QPushButton("Retour")
        home_btn.clicked.connect(self.cours)
        self.cours_tab.layout().addWidget(home_btn)

    

    def add_cours(self):
        self.clear_frame(self.cours_tab)
        form_frame = QWidget()
        form_layout = QFormLayout()
        form_frame.setLayout(form_layout)
        self.cours_tab.layout().addWidget(form_frame)

        frame_title = QLabel("Ajout de cours")
        frame_title.setFont(self.font())
        form_layout.addRow(frame_title)

        nom_label = QLabel("Nom:")
        self.nom_entry = QLineEdit()
        form_layout.addRow(nom_label, self.nom_entry)

        description_label = QLabel("Description:")
        self.description_entry = QLineEdit()
        form_layout.addRow(description_label, self.description_entry)

        button_submit = QPushButton("Ajouter")
        button_submit.clicked.connect(self.submit_form_cours)
        form_layout.addWidget(button_submit)

    def submit_form_cours(self):
        nom = self.nom_entry.text()
        description = self.description_entry.text()
        create_cours(nom, description)
        self.clear_frame(self.cours_tab)
        self.cours()

    def delete_cours(self):
        self.clear_frame(self.cours_tab)
        form_frame = QWidget()
        form_layout = QFormLayout()
        form_frame.setLayout(form_layout)
        self.cours_tab.layout().addWidget(form_frame)

        frame_title = QLabel("Delete Cours")
        frame_title.setFont(self.font())
        form_layout.addRow(frame_title)

        id_label = QLabel("Id:")
        self.id_entry = QLineEdit()
        form_layout.addRow(id_label, self.id_entry)

        button_submit = QPushButton("Delete")
        button_submit.clicked.connect(self.submit_delete_cours)
        form_layout.addWidget(button_submit)

    def submit_delete_cours(self):
        id = self.id_entry.text()
        delete_cours(id)
        self.clear_frame(self.cours_tab)
        self.cours()
    

    def update_cours(self):
        self.clear_frame(self.cours_tab)  
        form_frame = QWidget()
        form_layout = QFormLayout()
        form_frame.setLayout(form_layout)
        self.cours_tab.layout().addWidget(form_frame)

        frame_title = QLabel("Update Cours")
        frame_title.setFont(self.font())
        form_layout.addRow(frame_title)

        id_label = QLabel("Id:")
        self.id_entry = QLineEdit()
        form_layout.addRow(id_label, self.id_entry)

        nom_label = QLabel("nom_cours:")
        self.nom_entry = QLineEdit()
        form_layout.addRow(nom_label, self.nom_entry)

        prenom_label = QLabel("description :")
        self.prenom_entry = QLineEdit()
        form_layout.addRow(prenom_label, self.prenom_entry)

        button_submit = QPushButton("Update :")
        button_submit.clicked.connect(self.submit_update)
        form_layout.addWidget(button_submit)

    def submit_update(self):
        id = self.id_entry.text()
        nom_cours = self.nom_entry.text()
        description = self.prenom_entry.text()
        result = update_cours_description(id, nom_cours,description )

        if result == 0:
            print("cours introuvable, mise à jour non effectuée")
        else:
            self.clear_frame(self.utilisateurs_tab)
            self.cours()


    def salle(self):
        existing_layout_salles = self.salles_tab.layout()
        if existing_layout_salles:
            QWidget().setLayout(existing_layout_salles)
        self.tab_widget.setCurrentIndex(3)
        form_layout_salles = QVBoxLayout() 
        self.salles_tab.setLayout(form_layout_salles) 
         
        frame_title = QLabel("Gestion des salles :")
        font = frame_title.font()
        font.setBold(True)  
        frame_title.setFont(font)
        frame_title.setStyleSheet("color: blue;")  
        form_layout_salles.addWidget(frame_title)
        

       
        list_button = QPushButton("Liste des Salles")
        list_button.clicked.connect(self.display_salles)
        form_layout_salles.addWidget(list_button)
        
        add_button = QPushButton("ajouter Salles")
        add_button.clicked.connect(self.add_salles)
        form_layout_salles.addWidget(add_button)

        edit_button = QPushButton("editer Salles")
        edit_button.clicked.connect(self.update_salle)
        form_layout_salles.addWidget(edit_button)

        delete_button = QPushButton("supprimer Salles")
        delete_button.clicked.connect(self.delete_salle)
        form_layout_salles.addWidget(delete_button)


    
    def display_salles(self):
        self.clear_frame(self.salles_tab)
        
        existing_layout = self.salles_tab.layout()
        if existing_layout:
            QWidget().setLayout(existing_layout)

        salles = get_all_salles()
        form_layout_salles = QVBoxLayout()
        self.salles_tab.setLayout(form_layout_salles)

        table = QTreeWidget()
        table.setHeaderLabels(["ID", "Nom", "Capacite"])
        form_layout_salles.addWidget(table)  

        for salle in salles:
            item = QTreeWidgetItem(table)
            item.setText(0, str(salle[0]))  
            item.setText(1, salle[1])
            item.setText(2, str(salle[2]))  

        home_btn = QPushButton("Retour")
        home_btn.clicked.connect(self.salle)
        form_layout_salles.addWidget(home_btn)  

     
    def add_salles(self):
        self.clear_frame(self.salles_tab)
        form_frame = QWidget()
        form_layout = QFormLayout()
        form_frame.setLayout(form_layout)
        self.salles_tab.layout().addWidget(form_frame)  

        frame_title = QLabel("Ajout de salle")
        frame_title.setFont(self.font())
        form_layout.addRow(frame_title)

        nom_label = QLabel("nom_salle:")
        self.nom_entry = QLineEdit()
        form_layout.addRow(nom_label, self.nom_entry)

        description_label = QLabel("capacite:")
        self.capacite_entry = QLineEdit()
        form_layout.addRow(description_label, self.capacite_entry)

        button_submit = QPushButton("Ajouter")
        button_submit.clicked.connect(self.submit_form_salle)
        form_layout.addWidget(button_submit)
        
    def submit_form_salle(self):
        nom_salle = self.nom_entry.text()
        capacite = self.capacite_entry.text()
        create_salle(nom_salle, capacite)
        self.clear_frame(self.salles_tab)
        self.salle()

    def update_salle(self):
        self.clear_frame(self.salles_tab)  
        form_frame = QWidget()
        form_layout = QFormLayout()
        form_frame.setLayout(form_layout)
        self.salles_tab.layout().addWidget(form_frame)  

        frame_title = QLabel("Update Salle")
        frame_title.setFont(self.font())
        form_layout.addRow(frame_title)

        id_label = QLabel("Id:")
        self.id_entry = QLineEdit()
        form_layout.addRow(id_label, self.id_entry)

        nom_label = QLabel("nom_salle:")
        self.nom_entry = QLineEdit()
        form_layout.addRow(nom_label, self.nom_entry)

        prenom_label = QLabel("capacite:")
        self.prenom_entry = QLineEdit()
        form_layout.addRow(prenom_label, self.prenom_entry)

        button_submit = QPushButton("Update")
        button_submit.clicked.connect(self.submit_update)
        form_layout.addWidget(button_submit)

    

    def delete_salle(self):
        self.clear_frame(self.salles_tab)  
        form_frame = QWidget()
        form_layout = QFormLayout()
        form_frame.setLayout(form_layout)
        self.salles_tab.layout().addWidget(form_frame)  

        frame_title = QLabel("Delete Salle")
        frame_title.setFont(self.font())
        form_layout.addRow(frame_title)

        id_label = QLabel("Id:")
        self.id_entry = QLineEdit()
        form_layout.addRow(id_label, self.id_entry)

        button_submit = QPushButton("Delete")
        button_submit.clicked.connect(self.submit_delete_salle)
        form_layout.addWidget(button_submit)


    def submit_delete_salle(self):
        id = self.id_entry.text()
        delete_salle(id)
        self.clear_frame(self.cours_tab)
        self.salle()
          

    def emploi(self):
        existing_layout = self.emploi_tab.layout()
        if existing_layout:
            QWidget().setLayout(existing_layout)
        self.tab_widget.setCurrentIndex(4)
        form_layout = QVBoxLayout()  
        self.emploi_tab.setLayout(form_layout)  
        
        frame_title = QLabel("Gestion d'Emplois :")
        font = frame_title.font()
        font.setBold(True)  
        frame_title.setFont(font)
        frame_title.setStyleSheet("color: blue;")  
        form_layout.addWidget(frame_title)
        

        list_button = QPushButton("Liste des Emplois")
        list_button.clicked.connect(self.display_emploi)
        form_layout.addWidget(list_button)

        add_button = QPushButton("ajouter Emplois")
        add_button.clicked.connect(self.add_emploi)
        form_layout.addWidget(add_button)

        edit_button = QPushButton("editer Emplois")
        edit_button.clicked.connect(self.update_emploi)
        form_layout.addWidget(edit_button)

        delete_button = QPushButton("supprimer Emplois")
        delete_button.clicked.connect(self.delete_emploi)
        form_layout.addWidget(delete_button)
    

    def display_emploi(self):
        self.clear_frame(self.emploi_tab)
        
        existing_layout = self.emploi_tab.layout()
        if existing_layout:
            QWidget().setLayout(existing_layout)

        emploidutemps = get_all_emploidutemps()

        form_layout_emploi = QVBoxLayout()
        self.emploi_tab.setLayout(form_layout_emploi)

        table = QTreeWidget()
        table.setHeaderLabels(["ID", "Jour de la semaine", "Heure de début", "Heure de fin", "Cours ID", "Utilisateur ID", "Salle ID"])
        form_layout_emploi.addWidget(table)  

        for emploi in emploidutemps:
            item = QTreeWidgetItem(table)
            item.setText(0, str(emploi[0]))  
            item.setText(1, emploi[1])
            item.setText(2, emploi[2])
            item.setText(3, emploi[3])
            item.setText(4, str(emploi[4]))
            item.setText(5, str(emploi[5]))
            item.setText(6, str(emploi[6]))

        home_btn = QPushButton("Retour")
        home_btn.clicked.connect(self.emploi)
        form_layout_emploi.addWidget(home_btn)  


     
    def add_emploi(self):
        self.clear_frame(self.emploi_tab)
        form_frame = QWidget()
        form_layout = QFormLayout()
        form_frame.setLayout(form_layout)
        self.emploi_tab.layout().addWidget(form_frame)  

        frame_title = QLabel("Ajout d'emploi du temps")
        frame_title.setFont(self.font())
        form_layout.addRow(frame_title)

        jour_semaine_label = QLabel("Jour de la semaine:")
        self.jour_semaine_entry = QLineEdit()
        form_layout.addRow(jour_semaine_label, self.jour_semaine_entry)

        heure_debut_label = QLabel("Heure de début:")
        self.heure_debut_entry = QLineEdit()
        form_layout.addRow(heure_debut_label, self.heure_debut_entry)

        heure_fin_label = QLabel("Heure de fin:")
        self.heure_fin_entry = QLineEdit()
        form_layout.addRow(heure_fin_label, self.heure_fin_entry)

        cours_id_label = QLabel("Cours ID:")
        self.cours_id_entry = QLineEdit()
        form_layout.addRow(cours_id_label, self.cours_id_entry)

        utilisateur_id_label = QLabel("Utilisateur ID:")
        self.utilisateur_id_entry = QLineEdit()
        form_layout.addRow(utilisateur_id_label, self.utilisateur_id_entry)

        salle_id_label = QLabel("Salle ID:")
        self.salle_id_entry = QLineEdit()
        form_layout.addRow(salle_id_label, self.salle_id_entry)

        button_submit = QPushButton("Ajouter")
        button_submit.clicked.connect(self.submit_form_emploi)
        form_layout.addWidget(button_submit)

    def submit_form_emploi(self):
        jour_semaine = self.jour_semaine_entry.text()
        heure_debut = self.heure_debut_entry.text()
        heure_fin = self.heure_fin_entry.text()
        cours_id = self.cours_id_entry.text()
        utilisateur_id = self.utilisateur_id_entry.text()
        salle_id = self.salle_id_entry.text()
        
        create_emploidutemps(jour_semaine, heure_debut, heure_fin, cours_id, utilisateur_id, salle_id)
        self.clear_frame(self.emploi_tab)
        self.emploi() 

    def update_emploi(self):
        self.clear_frame(self.emploi_tab)
        form_frame = QWidget()
        form_layout = QFormLayout()
        form_frame.setLayout(form_layout)
        self.emploi_tab.layout().addWidget(form_frame)  

        frame_title = QLabel("Mise à jour d'emploi du temps")
        frame_title.setFont(self.font())
        form_layout.addRow(frame_title)

        id_label = QLabel("ID de l'emploi du temps à mettre à jour:")
        self.id_entry = QLineEdit()
        form_layout.addRow(id_label, self.id_entry)

        jour_semaine_label = QLabel("Nouveau jour de la semaine:")
        self.jour_semaine_entry = QLineEdit()
        form_layout.addRow(jour_semaine_label, self.jour_semaine_entry)

        heure_debut_label = QLabel("Nouvelle heure de début:")
        self.heure_debut_entry = QLineEdit()
        form_layout.addRow(heure_debut_label, self.heure_debut_entry)

        heure_fin_label = QLabel("Nouvelle heure de fin:")
        self.heure_fin_entry = QLineEdit()
        form_layout.addRow(heure_fin_label, self.heure_fin_entry)

        cours_id_label = QLabel("Nouveau Cours ID:")
        self.cours_id_entry = QLineEdit()
        form_layout.addRow(cours_id_label, self.cours_id_entry)

        utilisateur_id_label = QLabel("Nouveau Utilisateur ID:")
        self.utilisateur_id_entry = QLineEdit()
        form_layout.addRow(utilisateur_id_label, self.utilisateur_id_entry)

        salle_id_label = QLabel("Nouveau Salle ID:")
        self.salle_id_entry = QLineEdit()
        form_layout.addRow(salle_id_label, self.salle_id_entry)

        button_submit = QPushButton("Mettre à jour")
        button_submit.clicked.connect(self.submit_update_emploi)
        form_layout.addWidget(button_submit)

    def submit_update_emploi(self):
        emploi_id = self.id_entry.text()
        jour_semaine = self.jour_semaine_entry.text()
        heure_debut = self.heure_debut_entry.text()
        heure_fin = self.heure_fin_entry.text()
        cours_id = self.cours_id_entry.text()
        utilisateur_id = self.utilisateur_id_entry.text()
        salle_id = self.salle_id_entry.text()
        
        update_emploidutemps(emploi_id, jour_semaine, heure_debut, heure_fin, cours_id, utilisateur_id, salle_id)
        self.clear_frame(self.emploi_tab)
        self.emploi()  


    def delete_emploi(self):
        self.clear_frame(self.emploi_tab)
        form_frame = QWidget()
        form_layout = QFormLayout()
        form_frame.setLayout(form_layout)
        self.emploi_tab.layout().addWidget(form_frame)  

        frame_title = QLabel("Supprimer l'emploi du temps")
        frame_title.setFont(self.font())
        form_layout.addRow(frame_title)

        id_label = QLabel("ID de l'emploi du temps à supprimer:")
        self.id_entry = QLineEdit()
        form_layout.addRow(id_label, self.id_entry)

        button_submit = QPushButton("Supprimer")
        button_submit.clicked.connect(self.submit_delete_emploi)
        form_layout.addWidget(button_submit)

    def submit_delete_emploi(self):
        emploi_id = self.id_entry.text()
        delete_emploidutemps(emploi_id)
        self.clear_frame(self.emploi_tab)
        self.emploi()  

   

def main():
    app = QApplication(sys.argv)
    fen = App()
    fen.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()