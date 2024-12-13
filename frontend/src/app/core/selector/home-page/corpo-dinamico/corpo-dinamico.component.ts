import { Component } from '@angular/core';
import { MinimumCards, TypeCardsEnum } from '../../../../shared/models/cards.model';

@Component({
  selector: 'app-corpo-dinamico',
  templateUrl: './corpo-dinamico.component.html',
  styleUrl: './corpo-dinamico.component.css'
})
export class CorpoDinamicoComponent {


  games: MinimumCards[] = [
    {
      tipo: TypeCardsEnum.BARALHO,
      nome: 'Truco',
      classificacao: '18'
    },
    {
      tipo: TypeCardsEnum.PAPEL,
      nome: 'Stop',
      classificacao: 'Livre'
    }
  ];
}
