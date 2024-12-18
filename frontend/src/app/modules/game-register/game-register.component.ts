import { Component } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
import { ClassificacaoCards, TypeCardsEnum } from '../../shared/models/cards.model';
import { PythonService } from '../../shared/services/python.service';

@Component({
  selector: 'app-game-register',
  templateUrl: './game-register.component.html',
  styleUrl: './game-register.component.css'
})
export class GameRegisterComponent {

  form: FormGroup = new FormGroup({
    nomeJogo: new FormControl(),
    regraJogo: new FormControl(),
    minJogadores: new FormControl(),
    maxJogadores: new FormControl(),
    tipoJogo: new FormControl('Selecione o tipo'),
    faixaEtaria: new FormControl('Selecione a faixa etária')
  })

  tiposJogo!: { value: string; label: string }[];
  faixasEtarias!: { value: string; label: string }[];

  constructor(
    private service: PythonService
  ) {
    this.tiposJogo = this.enumToArray(TypeCardsEnum);
    this.faixasEtarias = this.enumToArray(ClassificacaoCards);
  }

  enumToArray(enumObj: any): { value: string; label: string }[] {
    return Object.keys(enumObj).map(key => ({
      value: enumObj[key], // Valor real do enum
      label: key.charAt(0).toUpperCase() + key.slice(1).toLowerCase() // Exibe o nome formatado
    }));
  }

  register(): void {
    this.service.cadastroJogo(this.form.value).subscribe({
      next: () => {
        console.log("deu certo")
      },
      error: () => {
        console.log("deu erro");
      }
    })
  };
}


