import { Component } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';

@Component({
  selector: 'app-game-register',
  templateUrl: './game-register.component.html',
  styleUrl: './game-register.component.css'
})
export class GameRegisterComponent {

  form: FormGroup = new FormGroup({
    nomeJogo: new FormControl(),
    regraJogo: new FormControl(),
    numeroJogadores: new FormControl(),
    tipoJogo: new FormControl(),
    faixaEtaria: new FormControl()
  })

  constructor(){}

  register(): void {

  }

}
