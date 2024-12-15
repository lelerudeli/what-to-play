import { Component } from '@angular/core';
import { ClassificacaoCards, MinimumCards, TypeCardsEnum } from '../../shared/models/cards.model';
import { PythonService } from '../../shared/services/python.service';
import { Observable, of } from 'rxjs';
import { Jogo } from '../../shared/models/jogo.model';

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
      classificacao: ClassificacaoCards.DEZOITO
    },
    {
      tipo: TypeCardsEnum.PAPEL,
      nome: 'Stop',
      classificacao: ClassificacaoCards.LIVRE
    }
  ];

  games$: Observable<Jogo[]> = of([]);

  constructor(
    private service: PythonService
  ) { }

  ngOnInit(): void {
    this.getAllGames();
  }

  getAllGames(): void {
    this.games$ = this.service.getAllJogos();
  }
}
