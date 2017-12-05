// Commande d'un moteur pas-à-pas à l'aide d'un pilote DRV8825 avec
//     Arduino.  1tour 8mm 200pas

//2 MOTEURS DU BAS pin
#define vertiPinEnable 7 // Activation du driver/pilote
#define vertiPinStep  6 // Signal de PAS (avancement)
#define vertiPinDir     5 // Direction 
#define vertiPinEndstop_bottom 2 // pin du endstop 


// MOTEUR DU HAUT pin
#define horizPinEnable  12 // Activation du driver/pilote
#define horizPinStep    11 // Signal de PAS (avancement)
#define horizPinDir     10 // Direction 
#define horizPinEndstop_left 3 // pin du endstop 


//Nb step max par axe (nb pas)
#define vertiNbStepMax 1000 //(pas)
#define horizNbStepMax 1000 //(pas)

//Fonction Arrosage
#define courseSpray 200 //(pas) 


// Zones de Danger axes (pots de fleurs) (%)
#define minVertiDangerZoneHigh 60 //(%)
#define maxVertiDangerZoneHigh 80 //(%)
#define vertiDangerZoneLow 10 //(%)
#define horizPercentSafeZone 50 //(%)
#define leftSprayZone 25 //(%)
#define rightSprayZone 75 //(%)



///// Variables globales ///////////
long horizCurrentPos = 123456;
long vertiCurrentPos = 123456;

long horizMinPos = 0;
long vertiMinPos = 0;

int tempoSpray = 8000; // Temps D'arrosage.

// Communication Série
String msg = "";
boolean cmp = false;


void setup() {
  Serial.begin(9600);
  //msg.reserve(8);

  Serial.println("Let's go !");

  pinMode( horizPinEnable, OUTPUT );
  pinMode( horizPinDir   , OUTPUT );
  pinMode( horizPinStep  , OUTPUT );
  pinMode (horizPinEndstop_left , INPUT);

  pinMode( vertiPinEnable, OUTPUT );
  pinMode( vertiPinDir   , OUTPUT );
  pinMode( vertiPinStep  , OUTPUT );
  pinMode(vertiPinEndstop_bottom , INPUT);

  horizCurrentPos = 123456;
  vertiCurrentPos = 123456;
  disableMotor (0);
  disableMotor (1);
}



void loop()
{
  /*
    if (cmp) {

      interpret();
      cmp = false;
      msg = "";
    }
  */



  Serial.println("Original current position : ");
  Serial.println(horizCurrentPos);
  initMotor();

  delay(2000);
  goTo (25, 30);
  Serial.println("horiz current position : ");
  Serial.println(horizCurrentPos);
  Serial.println(" verti current position : ");
  Serial.println(vertiCurrentPos);
  delay(4000);

  //    goTo (25, 82);
  //    Serial.println("horiz current position : ");
  //    Serial.println(horizCurrentPos);
  //    Serial.println(" verti current position : ");
  //    Serial.println(vertiCurrentPos);
  //    delay(4000);
  //
  //
  //    goTo (80, 40);
  //    Serial.println("horiz current position : ");
  //    Serial.println(horizCurrentPos);
  //    Serial.println(" verti current position : ");
  //    Serial.println(vertiCurrentPos);
  //    delay(4000);
  //
  //    goTo (25, 10);
  //    Serial.println("horiz current position : ");
  //    Serial.println(horizCurrentPos);
  //    Serial.println(" verti current position : ");
  //    Serial.println(vertiCurrentPos);
  //    delay(4000);



  // goTo (50, 20);
  disableMotor (0);
  delay(2000);
  disableMotor (1);
  while (true);

}


int initMotor ()
{
  horizCurrentPos = 4321; // eviter boucle infinie.
  vertiCurrentPos = 4321; // eviter boucle infinie.
  int retour, retour2 = 0;
  retour = driveMotor (0, 0, 20000, 5); //go taper a gauche
  delay(1000);
  long center = (((long)horizPercentSafeZone * (long)horizNbStepMax) / 100);
  driveMotor (0, 1, center, 5); // go au centre
  delay(1000);
  retour2 = driveMotor (1, 0, 20000, 5); //go taper en bas

  if (vertiCurrentPos != 0 )
  {
    return -1;
  }

  delay(1000);
  long offsetBottom = (((long)vertiDangerZoneLow * (long)vertiNbStepMax) / 100);
  driveMotor (1, 1, offsetBottom, 5); // go vertiZoneLow
  disableMotor (0);
  delay(2000);
  disableMotor (1);
  return 0;
}


int disableMotor (int numMotor)
{
  if (numMotor == 0) // moteur du haut
  {
    // déblocage de l'axe moteur
    digitalWrite( horizPinEnable, HIGH ); // logique inversée
  }
  else if (numMotor == 1) //moteur du bas
  {
    // déblocage de l'axe moteur
    digitalWrite( vertiPinEnable, HIGH ); // logique inversée
  }
}


int driveMotor (int numMotor, int dir, long nbStep, int SpeedMotor)
{
  Serial.println("Alert : DriveMotor en cours...");
  if ( horizCurrentPos == 123456 ) // Un init() doit être fait.
  {
    initMotor();
    Serial.println("Alert : Init Forcé horiz");
  }
  else if (vertiCurrentPos == 123456) // Un init() doit être fait.
  {
    initMotor();
    Serial.println("Alert : Init Forcé verti");

  }

  int pinDir = 0;
  int pinStep = 0;
  int valuePinEndstop = 0;
  int pinEnable = 0;
  int retour = 99;

  long minPos = 0;
  long currentPos = 0;
  long nbStepMax = 0;

  if (numMotor == 0) // moteur du haut
  {
    pinDir = horizPinDir;
    pinStep = horizPinStep;
    valuePinEndstop = horizPinEndstop_left;
    pinEnable = horizPinEnable;
    nbStepMax = horizNbStepMax;
    if (dir == 0)
    {
      dir = 1;
    }
    else
    {
      dir = 0;
    }
  }

  else if (numMotor == 1)
  {
    pinDir = vertiPinDir;
    pinStep = vertiPinStep;
    valuePinEndstop = vertiPinEndstop_bottom;
    pinEnable = vertiPinEnable;
    nbStepMax = vertiNbStepMax;
  }

  if (SpeedMotor < 5)
  {
    SpeedMotor = 5;
  }

  //blocage de l'axe moteur
  digitalWrite(pinEnable, LOW ); // logique inversée

  if (dir == 0)
  {
    digitalWrite( pinDir   , LOW); // Direction arrière CCW
  }
  else
  {
    digitalWrite( pinDir   , HIGH); // Direction avant CW
    if (nbStep > (nbStepMax - currentPos))
    {
      nbStep = (nbStepMax - currentPos); // Sécurité pour ne pas depasser le nombre de pas maximum par axe.
      Serial.println("Alert : Consigne trop élevé");
    }
  }

  digitalWrite( pinStep  , LOW);  // Initialisation de la broche step

  long i = 0;
  for (i = 0; i < nbStep; i++)
  {
    if (numMotor == 1)
    {
      if (dir == 1)
      {
        currentPos++;
      }
      else
      {
        currentPos--;
      }
    }
    else
    {
      if (dir == 0)
      {
        currentPos++;
      }
      else
      {
        currentPos--;
      }
    }
      Serial.println(currentPos);


    digitalWrite( pinStep, HIGH );

    if (digitalRead(valuePinEndstop) == LOW) // si on touche le endstop.
    {
      if (dir == 0)
      {
        dir = 1;
      }
      else
      {
        dir = 0;
      }
      if (dir == 0)
      {
        digitalWrite( pinDir   , LOW); // Direction arrière CCW
      }
      else
      {
        digitalWrite( pinDir   , HIGH); // Direction avant CW
      }
      minPos = currentPos = 0;
      if (numMotor == 0) // moteur du haut
      {
        horizCurrentPos = currentPos;
        horizMinPos = minPos;
      }
      else if (numMotor == 1)
      {
        vertiCurrentPos = currentPos;
        vertiMinPos = minPos;
      }
      int j = 0;
      for (j = 0; j < 50; j++)
      {
        digitalWrite( pinStep, HIGH );
        delay(SpeedMotor);
        digitalWrite( pinStep, LOW );
      }
      if (dir == 0)
      {
        dir = 1;
      }
      else
      {
        dir = 0;
      }
      if (dir == 0)
      {
        digitalWrite( pinDir   , LOW); // Direction arrière CCW
      }
      else
      {
        digitalWrite( pinDir   , HIGH); // Direction avant CW
      }
      break;
    }

    delay(SpeedMotor);
    digitalWrite( pinStep, LOW );

    if (digitalRead(valuePinEndstop) == LOW)// si on touche le endstop.
    {
      if (dir == 0)
      {
        dir = 1;
      }
      else
      {
        dir = 0;
      }
      if (dir == 0)
      {
        digitalWrite( pinDir   , LOW); // Direction arrière CCW
      }
      else
      {
        digitalWrite( pinDir   , HIGH); // Direction avant CW
      }
      int j = 0;
      for (j = 0; j < 50; j++)
      {
        digitalWrite( pinStep, HIGH );
        delay(SpeedMotor);
        digitalWrite( pinStep, LOW );
      }
      if (dir == 0)
      {
        dir = 1;
      }
      else
      {
        dir = 0;
      }
      if (dir == 0)
      {
        digitalWrite( pinDir   , LOW); // Direction arrière CCW
      }
      else
      {
        digitalWrite( pinDir   , HIGH); // Direction avant CW
      }
      minPos = currentPos = 0;
      if (numMotor == 0) // moteur du haut
      {
        horizCurrentPos = currentPos;
        horizMinPos = minPos;
      }
      else if (numMotor == 1)
      {
        vertiCurrentPos = currentPos;
        vertiMinPos = minPos;
      }
      break;
    }
    delay(SpeedMotor);
  }//end loop

  if (numMotor == 0) // moteur du haut
  {
    horizCurrentPos += currentPos;

  }
  else if (numMotor == 1)
  {
    vertiCurrentPos += currentPos;
  }
  if (retour != 0)
  {
    retour = 1;
  }
  return retour; // position atteinte sans interruption.
}




int goTo (int x, int y)
{
  Serial.println("Alert : Goto Function");
  long horizPercentCurrentPos = 0;
  long vertiPercentCurrentPos = 0;
  long horizPercentNextPos = 0;
  long vertiPercentNextPos = 0;
  bool otherCondition = false;
  x = (long)x;
  y = (long)y;

  //CONVERSION EN %  //////////////////////////

  horizPercentCurrentPos = ((horizCurrentPos * 100) / (long)horizNbStepMax) + 1;
  vertiPercentCurrentPos = ((vertiCurrentPos * 100) / (long)vertiNbStepMax) + 1;
  Serial.println("horizPercentCurrentPos");
  Serial.println(horizPercentCurrentPos);
  Serial.println("vertiPercentCurrentPos");
  Serial.println(vertiPercentCurrentPos);

  //CONDITIONS POUR DEPLACEMENTS 2 AXES ///////////////
  if ((vertiPercentCurrentPos <= minVertiDangerZoneHigh) && (vertiPercentCurrentPos >= vertiDangerZoneLow)) // ZONE BASSE
  {
    Serial.println("Pos ZONE CENTRALE");
    if (y < vertiPercentCurrentPos) // ON DESCENT
    {
      Serial.println("Nextpos ON DESCENT");
      if ( y > vertiDangerZoneLow) // nous sommes zone basse on veut aller encore plus bas.
      {
        vertiPercentNextPos = y;
        horizPercentNextPos = x;
      }
      else // DANGER zone basse pots
      {
        Serial.println("DANGER : Nextpos on va en limite low ! ");
        vertiPercentNextPos = vertiDangerZoneLow;
        horizPercentNextPos = x;
      }
    }

    else if (y > vertiPercentCurrentPos) // ON MONTE
    {
      Serial.println("Nextpos ON MONTE");
      if (y < minVertiDangerZoneHigh) // nous sommes zone basse et destination reste zone basse.
      {
        Serial.println("Nextpos on monte et reste zone centrale ");
        vertiPercentNextPos = y;
        horizPercentNextPos = x;
      }
      else if (y > minVertiDangerZoneHigh)// nous sommes zone basse on veut aller zone haute ou sur un pot.
      {
        Serial.println("Nextpos on va en ZONE HAUTE");
        if ( y < maxVertiDangerZoneHigh) // DANGER zone ascenseur
        {
          Serial.println("DANGER : position x fixée");
          horizPercentNextPos = horizPercentSafeZone;
          vertiPercentNextPos = y;
        }
        else // on monte en haut
        {
          Serial.println("Nextpos on monte tout en haut (+ otherCondition)");
          horizPercentNextPos = horizPercentSafeZone;
          vertiPercentNextPos = y;
          otherCondition = true; // on devra par la suite respecter la valeur x
        }
      }
    }
    else // ON RESTE MEME HAUTEUR // SEUL X CHANGE
    {
      vertiPercentNextPos = y;
      horizPercentNextPos = x;
    }
  }
  else if ((vertiPercentCurrentPos > minVertiDangerZoneHigh) && (vertiPercentCurrentPos < maxVertiDangerZoneHigh)) // CAGE D'ASCENSEUR ENTRE POTS SUSPENDUS
  {
    Serial.println("ON EST EN ZONE CAGE ASCENSEUR");
    if (y < vertiPercentCurrentPos) // ON DESCENT
    {
      if (y <= minVertiDangerZoneHigh) // On va en Zone Basse
      {
        if (y < vertiDangerZoneLow) // DANGER zone basse
        {
          horizPercentNextPos = horizPercentSafeZone;
          vertiPercentNextPos = vertiDangerZoneLow;
          otherCondition = true; // on devra par la suite respecter la valeur x
        }
        else
        {
          horizPercentNextPos = horizPercentSafeZone;
          vertiPercentNextPos = y; // on peut monter et descendre de 0 a 100%
          otherCondition = true; // on devra par la suite respecter la valeur x
        }
      }
      else
      {
        horizPercentNextPos = horizPercentSafeZone;
        vertiPercentNextPos = y; // on peut monter et descendre de 0 a 100%
      }
    }
    else if (y > vertiPercentCurrentPos) // ON MONTE
    {
      if (y >= maxVertiDangerZoneHigh) // On va en Zone haute
      {
        horizPercentNextPos = horizPercentSafeZone;
        vertiPercentNextPos = y; // on peut monter et descendre de 0 a 100%
        otherCondition = true; // on devra par la suite respecter la valeur x
      }
      else
      {
        horizPercentNextPos = horizPercentSafeZone;
        vertiPercentNextPos = y; // on peut monter et descendre de 0 a 100%
      }
    }
    else // On bouge pas
    {
      horizPercentNextPos = horizPercentSafeZone;
    }
  }

  else if (vertiPercentCurrentPos >= maxVertiDangerZoneHigh) /////////////////////////////////////////////////// ZONE HAUTE
  {
    Serial.println("ON EST EN ZONE HAUTE");
    if (y < vertiPercentCurrentPos) // ON DESCENT
    {
      Serial.println("Nextpos on DESCENT");
      if ( y >= maxVertiDangerZoneHigh) // nous sommes zone haute on veut aller zone haute plus bas.
      {
        Serial.println("Nextpos  on descent mais zone haute toujours");
        horizPercentNextPos = x;
        vertiPercentNextPos = y;
      }
      else if ( y < maxVertiDangerZoneHigh) // nous sommes zone haute on veut aller zone basse.
      {
        Serial.println("Nextpos ZONE CENTRALE ou ascenceur");
        if (y > vertiDangerZoneLow) // zone basse safe
        {
          Serial.println("Nextpos ZONE CENTRALE + (otherCondition)");
          if (y <= minVertiDangerZoneHigh) // on descent en zone basse
          {
            horizPercentNextPos = horizPercentSafeZone;
            vertiPercentNextPos = y;
            otherCondition = true;
          }
          else // destination haut vers cage ascenseur
          {
            Serial.println("Nextpos ZONE ASCENSEUR");
            horizPercentNextPos = horizPercentSafeZone;
            vertiPercentNextPos = y;
          }
        }
        else // DANGER POT zone basse!
        {
          horizPercentNextPos = horizPercentSafeZone;
          vertiPercentNextPos = vertiDangerZoneLow;
          otherCondition = true;
        }
      }
    }
    else if (y >= vertiPercentCurrentPos) // ON MONTE
    {
      Serial.println("On monte");
      horizPercentNextPos = x;
      vertiPercentNextPos = y;
    }
  }
  else
  {
    Serial.println("ERREUR DE CONDITION... BREAK.");
    return -1;
  }


  ////////////////////////////////////////////// ON APPLIQUE LES CONDITIONS AUX MOTEURS ////////////////////////////////////
  Serial.println("On applique les conditions aux moteurs..");
  long horizNextPos = 0;
  long vertiNextPos = 0;
  int horizDirection = 99;
  int vertiDirection = 99;
  int driveMotorResult = 99; // init var de retour

  horizNextPos = ((horizPercentNextPos * (long)horizNbStepMax) / 100);
  vertiNextPos = ((vertiPercentNextPos * (long)vertiNbStepMax) / 100);

  if (horizCurrentPos < horizNextPos) // la position courante > à la prochaine = dir = 0;
  {
    horizDirection = 1;
    horizNextPos = horizNextPos - horizCurrentPos;
  }
  else
  {
    horizDirection = 0;
    horizNextPos = -(horizNextPos - horizCurrentPos);
  }

  if (vertiCurrentPos < vertiNextPos) // la position courante > à la prochaine = dir = 0;
  {
    vertiDirection = 1;
    vertiNextPos = vertiNextPos - vertiCurrentPos;
  }
  else
  {
    vertiDirection = 0;
    vertiNextPos = -(vertiNextPos - vertiCurrentPos);
  }
  Serial.println("Ordre moteur Horiz depuis goto : Consigne:");
  Serial.println(horizNextPos);
  driveMotorResult = driveMotor (0, horizDirection, horizNextPos, 20);  // Moteur horizontal (0)  int driveMotor (int numMotor, int dir, int nbStep, int SpeedMotor)
  if (driveMotorResult == -1)
  {
    //erreur moteur horizontal
  }
  Serial.println("Ordre moteur Verti depuis goto : Consigne:");
  Serial.println(vertiNextPos);
  driveMotorResult = driveMotor (1, vertiDirection, vertiNextPos, 20);  // Moteur vertical (1er)  int driveMotor (int numMotor, int dir, int nbStep, int SpeedMotor)
  if (driveMotorResult == -1)
  {
    //erreur moteur vertical
  }


  if (otherCondition == true) // On va se positionner en x , la cage d'ascenseur est passée.
  {
    Serial.println("OTHER CONDITION");
    horizPercentNextPos = x;
    otherCondition = false;
    horizNextPos = ((horizPercentNextPos * (long)horizNbStepMax) / 100);
    horizDirection = 99;

    if (horizCurrentPos < horizNextPos) // la position courante > à la prochaine = dir = 0
    {
      horizDirection = 1;
      horizNextPos = horizNextPos - horizCurrentPos;
    }
    else
    {
      horizDirection = 0;
      horizNextPos = - (horizNextPos - horizCurrentPos);
    }
    Serial.println("x");
    Serial.println(x);
    Serial.println("horizCurrentPos");
    Serial.println(horizCurrentPos);
    Serial.println("horizNextPos");
    Serial.println(horizNextPos);
    Serial.println("sens");
    Serial.println(horizDirection);


    driveMotorResult = driveMotor (0, horizDirection, horizNextPos, 20);  // Moteur horizontal (1er)  int driveMotor (int numMotor, int dir, int nbStep, int SpeedMotor)
    if (driveMotorResult == -1)
    {
      //erreur moteur horizontal
    }
  }


  ////////////////////////////////////////////// TEST FONCTIONS ARROSAGE ///////////////////////////////////////////////////
  if (y == maxVertiDangerZoneHigh)
  {
    if (x == leftSprayZone)
    {
      Serial.println("zone arrosage !");
      driveMotor(1, 0, courseSpray, 15);
      delay(tempoSpray);
      driveMotor(1, 1, courseSpray, 15);
    }
    else if (x == rightSprayZone)
    {
      Serial.println("zone arrosage !");
      driveMotor(1, 0, courseSpray, 15);
      delay(tempoSpray);
      driveMotor(1, 1, courseSpray, 15);
    }
  }
  else if (y == vertiDangerZoneLow)
  {
    if (x == leftSprayZone)
    {
      Serial.println("zone arrosage !");
      driveMotor(1, 0, courseSpray, 15);
      delay(tempoSpray);
      driveMotor(1, 1, courseSpray, 15);
    }
    else if (x == rightSprayZone)
    {
      Serial.println("zone arrosage !");
      driveMotor(1, 0, courseSpray, 15);
      delay(tempoSpray);
      driveMotor(1, 1, courseSpray, 15);
    }
  }
  return 0;
}


void interpret() {
  int arg[2];
  if ('W' == msg[0]) { // Who (identité arduino) : Message de réponse 2
    Serial.print('2');

  }
  else if ('G' == msg[0])  // GoTo(x;y)
  {
    arg[0] = (msg[1] - '0') * 10 + (msg[2] - '0');
    arg[1] = (msg[3] - '0') * 10 + (msg[4] - '0');

    char feedback = goTo(arg[0], arg[1]);
    //goTo (50, 20);
    disableMotor (0);
    delay(2000);
    disableMotor (1);
    Serial.print(feedback); // si O : Ok si K : KO

  }
  else if ('D' == msg[0])  // D de 1 à 9 -> 1000 a 9000 ms
  {
    tempoSpray = tempoSpray * msg[1];
  }
  else if ('I' == msg[0])
  {
    initMotor();
  }
  else
  {
    Serial.print('?');
  }
}

void serialEvent() {

  char c;

  while (Serial.available()) {

    char c = (char)Serial.read();
    msg += c;

    if (c == ';') {
      cmp = true;
    }
  }
}





