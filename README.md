# Tumorgroei modelleren

## 1. Projectbeschrijving

In dit project onderzoeken we de groei van een tumor aan de hand van wiskundige modellen en Ordinary Differential Equations (ODE's). Hiervoor gebruiken we meetgegevens van tumorvolume over een periode van 120 dagen.

Het doel is om verschillende tumorgroeimodellen te implementeren, de groei numeriek te berekenen en te onderzoeken welk model het beste aansluit bij de beschikbare meetgegevens.

## 2. Gebruikte modellen

We vergelijken drie verschillende groeimodellen:

- **Exponentieel groeimodel:** beschrijft groei waarbij de groeisnelheid afhankelijk is van de huidige tumorgrootte.
- **Logistisch groeimodel:** houdt rekening met een maximale tumoromvang (draagkracht).
- **Gompertz groeimodel:** beschrijft groei waarbij de groeisnelheid geleidelijk afneemt naarmate de tumor groter wordt.

## 3. ODE-solvers

Om de differentiaalvergelijkingen numeriek op te lossen, gebruiken we drie methoden:

- **Euler:** gebruikt de groeisnelheid aan het begin van een tijdstap.
- **Heun:** gebruikt het gemiddelde van de groeisnelheid aan het begin en einde van een voorspelde tijdstap.
- **Runge-Kutta 4 (RK4):** gebruikt vier groeisnelheden om een nauwkeurigere schatting te maken.

## 4. Parameteroptimalisatie

Met behulp van een Monte Carlo-simulatie testen we willekeurige parametercombinaties voor de groeimodellen.

Voor iedere combinatie berekenen we de Mean Squared Error (MSE). De parametercombinatie met de laagste MSE wordt geselecteerd als beste resultaat.

## 5. Modelvergelijking

De modellen worden met elkaar vergeleken op basis van de MSE en de daaruit berekende AIC en BIC. Hiermee onderzoeken we welk model de kleinste afwijking heeft ten opzichte van de oorspronkelijke meetgegevens.

Ook vergelijken we de verschillende ODE-solvers om te onderzoeken welke numerieke methode het beste resultaat geeft.

## 6. Benodigdheden

Het project is geschreven in Python.

Benodigde libraries:
- pandas
- matplotlib

De standaard Python-modules `math` en `random` worden ook gebruikt.

## 7. Uitvoeren

Start het project vanuit de hoofdmap met:

```bash
python tumor_model/main.py
```

Het programma leest de meetgegevens in, voert de groeimodellen en ODE-solvers uit, optimaliseert de modelparameters en toont de resultaten.

## 8. Resultaten

De resultaten worden gebruikt om de verschillende groeimodellen en ODE-solvers met elkaar te vergelijken. Het model met de laagste MSE heeft de kleinste gemiddelde gekwadrateerde afwijking ten opzichte van de meetgegevens.

De definitieve resultaten en conclusies worden toegevoegd in de use-case.
