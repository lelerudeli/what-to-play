import { Component } from '@angular/core';
import { ClassificacaoCards, MinimumCards, TypeCardsEnum } from '../../shared/models/cards.model';
import { PythonService } from '../../shared/services/python.service';
import { Observable, of } from 'rxjs';
import { Jogo } from '../../shared/models/jogo.model';

@Component({
  selector: 'app-all-games',
  templateUrl: './all-games.component.html',
  styleUrl: './all-games.component.css'
})
export class AllGamesComponent {

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
