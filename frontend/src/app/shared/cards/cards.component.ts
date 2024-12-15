import { Component, Input } from '@angular/core';
import { TypeCardsEnum } from '../models/cards.model';

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

  cardType = TypeCardsEnum;

  isFavorite = false;

  getCardImage(type: string) {
    switch (type) {
      case '1':
        return 'assets/baralho-removebg-preview.png';
      case '2':
        return 'assets/conversa-removebg-preview.png';
      default:
        return 'assets/papel-removebg-preview.png';
    }
  }
  getCardClassificacaoImage(classificacao: string) {
    switch (classificacao) {
      case 'DEZOITO':
        return 'assets/18.PNG';
      case 'DEZESSEIS':
        return 'assets/16.PNG';
      case 'CATORZE':
        return 'assets/14.PNG';
      case 'DOZE':
        return 'assets/12.PNG';
      case 'DEZ':
        return 'assets/10.PNG';
      default:
        return 'assets/livre.PNG';
    }
  }

  toggleCurtida(): void {
    this.isFavorite = !this.isFavorite;
  }

}
