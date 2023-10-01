const int bouton8 = 8; // Broche digitale 8
const int bouton2 = 2;
const int poten1 = 0;
int etatBouton8 = 1; // État actuel du bouton
int etatBouton2 = 1;
int etatPoten1 = 0;
int etatPoten1Pre = 0;
float potenPourcent = 0;

void setup() {
  pinMode(bouton8, INPUT); // Définit la broche du bouton comme une entrée
  pinMode(bouton2, INPUT);
  pinMode(poten1, INPUT);
  Serial.begin(9600); // Démarre la communication série à 9600 bauds
}

void loop() {
  etatBouton8 = digitalRead(bouton8); // Lit l'état actuel du bouton
  etatBouton2 = digitalRead(bouton2);
  etatPoten1 = analogRead(poten1);
  //Serial.println(etatBoutonActuel);
  // Vérifie si le bouton a été enfoncé
  if (etatBouton8 == 0) {
    Serial.println("b2");
    delay(200);
    // Vous pouvez ajouter ici le code que vous souhaitez exécuter lorsque le bouton est enfoncé
  }else if (etatBouton2 == 0){
    Serial.println("b1");
    delay(200);
  } 
}