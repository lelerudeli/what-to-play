import { Component } from '@angular/core';
import { MinimumCards, TypeCardsEnum } from '../../shared/models/cards.model';

@Component({
  selector: 'app-all-games',
  templateUrl: './all-games.component.html',
  styleUrl: './all-games.component.css'
})
export class AllGamesComponent {

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
