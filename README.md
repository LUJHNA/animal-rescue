# 🐾 Animal Rescue Webapplikation

_Udviklet af Jakob Husen_

![Animal Rescue Banner](https://images.pexels.com/photos/1254140/pexels-photo-1254140.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1)

## 📋 Introduktion

En webapplikation udviklet i Flask til at hjælpe dyreinternat med at holde styr på dyr og adoptioner. Systemet giver mulighed for at vise, filtrere og administrere dyr samt at håndtere adoptionsprocessen.

### Hovedfunktioner
- Visning af dyr med detaljer og billeder
- Avanceret filtrering og paginering
- Adoptionssystem med statussporing
- Responsivt design via Bootstrap

## 🛠️ Tekniske detaljer

### Flask
Et letforståeligt og fleksibelt Python web-framework, der gør det nemt at bygge webapplikationer. Flask giver frihed til at strukturere applikationen efter behov og er ideelt til mindre til mellemstore projekter.

### SQLAlchemy
Et kraftfuldt Object-Relational Mapping (ORM) bibliotek, der gør det muligt at arbejde med databasen ved hjælp af Python-objekter i stedet for rå SQL-kommandoer. Dette giver en mere intuitiv måde at interagere med data på.

### SQLite
En enkel filbaseret database, der er perfekt til mindre applikationer og udvikling. SQLite kræver ingen separat server og gemmer hele databasen i en enkelt fil, hvilket gør den ideel til dette projekt.

### Jinja2
En moderne og designer-venlig template engine for Python, der giver mulighed for at kombinere HTML med dynamisk indhold. Jinja2 understøtter template-arv, hvilket reducerer gentagelser i koden gennem et base-template system.

## ✨ Implementerede funktioner

### CRUD-operationer
Komplet understøttelse af Create, Read, Update og Delete for alle dyr i systemet:
- **Create**: Tilføj nye dyr til systemet
- **Read**: Se detaljer om individuelle dyr
- **Update**: Redigér information om eksisterende dyr
- **Delete**: Fjern dyr fra systemet

### Paginering og filtrering
- Avanceret filtrering efter dyrets art, køn og adoptionsstatus
- Paginering for bedre navigation ved mange dyr

### Adoptionssystem
- Workflow til håndtering af adoptionsprocessen
- Statussporing (Tilgængelig, Under behandling, Adopteret)
- Registrering af adoptanter med kontaktinformation

### Responsivt design
- Fuldt responsivt layout med Bootstrap
- Optimeret visning på både desktop og mobile enheder

## 🔄 Udfordringer og løsninger

### Database-relationer
Implementation af en-til-mange relation mellem adoptanter og dyr, hvilket muliggør sporing af, hvem der har adopteret hvilke dyr.

### Form-validering
Brug af Flask-WTF til validering af brugerinput, sikring af dataintegritet og forebyggelse af fejlindtastninger.

## 🚀 Fremtidige udvidelser

- **Brugerautentifikation**: Implementering af login-system for administratorer
- **Godkendelsesproces**: Workflow til godkendelse af adoptionsansøgninger
- **Rollebaseret adgang**: Kun administratorer kan tilføje/redigere/slette dyr
- **Sikkerhedsforbedringer**: Generel sikkerhedsoptimering
- **Filupload**: Direkte upload af dyrebilleder i stedet for URL-links
- **Statistik**: Visuel præsentation af adoptionsdata og trends

## 🔧 Installation og kørsel

```bash
# Klon repository
git clone https://github.com/yourusername/animal-rescue.git
cd animal-rescue

# Installer afhængigheder
pip install -r requirements.txt

# Kør applikationen
python app.py
```

## 📚 Kildefortegnelse

- [Flask-WTF dokumentation](https://flask-wtf.readthedocs.io/)
- [W3Schools](https://www.w3schools.com/)
- [SQLAlchemy dokumentation](https://www.sqlalchemy.org/)
- [Werkzeug dokumentation](https://werkzeug.palletsprojects.com/)
- [Flask-SQLAlchemy dokumentation](https://flask-sqlalchemy.palletsprojects.com/)
- [Jinja2 dokumentation](https://jinja.palletsprojects.com/en/stable/)
