import { Component } from '@angular/core';

@Component({
  selector: 'app-all-games',
  templateUrl: './all-games.component.html',
  styleUrl: './all-games.component.css'
})
export class AllGamesComponent {

  games = [
    { name: 'BURRO' },
    { name: 'ESPIÃO' },
    { name: 'TIBITAR' },
    { name: 'STOP' },
    { name: 'POKER' },
    { name: 'JOGO DA VELHA' },
    { name: 'ADOLETA' },
    { name: 'DETETIVE' },
  ];

}
