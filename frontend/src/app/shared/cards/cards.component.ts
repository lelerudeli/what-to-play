import { Component, Input } from '@angular/core';
import { MinimumCards, TypeCardsEnum } from '../models/cards.model';

@Component({
  selector: 'app-cards',
  templateUrl: './cards.component.html',
  styleUrl: './cards.component.css'
})
export class CardsComponent {

  @Input()
  type: string = '';

  @Input()
  name: string = '';

  @Input()
  classificacao: string = '';

  cards: MinimumCards[] = []

  cardType = TypeCardsEnum;

}
