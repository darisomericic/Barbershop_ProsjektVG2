# Torshov Perfect Cut – Booking Nettside

## 📌 Om prosjektet

Dette prosjektet er en fullstack nettside laget for frisørsalongen **Torshov Perfect Cut** i Oslo.

Nettsiden lar brukere se informasjon om salongen, priser og åpningstider, samt bestille time direkte gjennom en booking-modal.

Prosjektet er laget som en del av et skoleprosjekt for å vise forståelse av **frontend, backend og database**.

---

## ⚙️ Teknologier

Prosjektet bruker følgende teknologier:

### Frontend:

* Alt dynamisk som en nettside trenger og alt en bruker ser blir bygget opp i `React`

* UI, UX og responsivitet blir bygget opp i vanlig `CSS` 


### Backend

* Lagring av bestillinger og feilhåndtering skjer i `Flask`, som er en backend-rammeverk laget i `Python`

### Database

* Alle personoppysninger, og bestillinger blir lagret i `MariaDB`
---

## ✨ Funksjoner

Nettsiden inneholder følgende funksjonalitet:

* Forside med en hoved-seksjon 
* Navigasjonsmeny
* Prisliste (tabell)
* Åpningstider (tabell)
* Booking-modal
* Bestilling av time
* Lagring av alle bestillinger i en database


---

## 📋 Booking informasjon

Når en bruker bestiller en time lagres følgende informasjon:

* Fullt navn
* Telefonnummer
* Valgt tjeneste
* Dato
* Tidspunkt

Denne informasjonen sendes fra `React` frontend til `Flask` backend, som lagrer dataen i `MariaDB`.

---

## 🗄️ Database struktur

Eksempel på hvordan database-tabellen skal se ut:

### Menyen

| id | name       | price |
| -- | ---------- | ----- |
| 1  | Herreklipp | 350   |
| 2  | Barneklipp | 300   |
| 3  | Skjegg     | 200   |

### Bestillte timer 

| id | name | phone | service_id | date | time |
| -- | ---- | ----- | ---------- | ---- | ---- |

---

## 🧱 Prosjektstruktur

```


PROSJEKT_2_VG2/
├── barbershop/             # Frontend
│   ├── src/                # Kildekode 
│   │   ├── assets/
│   │   ├── pages/          # Sider
│   │   ├── App.jsx         # Main app
│   │   └── main.jsx
|   |
│   ├── public/             
│   ├── index.html        
│   ├── package.json        
│   └── vite.config.js 
|
├── app.py                  # Backend (Flask)
└── README.md               # Dokumentasjon
```

---

## 🚀 Hvordan kjøre prosjektet

### 1. Klon repo

```
git clone <repo-url>
```

### 2. Start backend

```
cd backend
python app.py
```

### 3. Start frontend

```
cd frontend
npm install
npm start
```

---

## 🎯 Mål med prosjektet

Målet med prosjektet her er å lære:

* hvordan bygge en fullstack nettside
* hvordan koble frontend til backend
* hvordan lagre data i en database
* hvordan lage et enkelt booking-system som lagres i databasen

---
