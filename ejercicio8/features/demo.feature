Feature: Feature Demo

Scenario: login correcto
  Given el usuario esta registrado
  When cuando introduce un nombre de usuario
  And cuando introduce su password
  And el usuario pulsa login
  Then el usuario accede al portal

  Scenario: login incorrecto
  Given el usuario esta registrado
  When cuando introduce un nombre falso de usuario
  And cuando introduce su password
  And el usuario pulsa login
  Then el usuario no puede acceder al portal
