import { Component } from '@angular/core';
import { PythonService } from '../../shared/services/python.service';
import { Profile } from '../../shared/models/perfil.model';
import { Observable, of } from 'rxjs';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrl: './profile.component.css'
})
export class ProfileComponent {

  users$: Observable<Profile> = of();

  arroba: string = '@';

  games = [
    { name: 'PIFE', description: 'até 8 jogadores • individual' },
    { name: 'TRUCO PAULISTA', description: '4 jogadores • em dupla' },
    { name: 'POKER', description: 'até 10 jogadores • individual' }
  ];

  activeTab: string = 'meusJogos';
  isFavorite = false;

  constructor(
    private service: PythonService
  ){}

  ngOnInit(): void {
    this.users$ = this.service.perfil();
  }

  setActiveTab(tab: string) {
    this.activeTab = tab;
  }

  toggleCurtida(): void {
    this.isFavorite = !this.isFavorite;
  }

  getCardClassificacaoImage(classificacao: string) {
    switch (classificacao) {
      case '18':
        return 'assets/18.PNG';
      case '16':
        return 'assets/16.PNG';
      case '14':
        return 'assets/14.PNG';
      case '12':
        return 'assets/12.PNG';
      case '10':
        return 'assets/10.PNG';
      default:
        return 'assets/livre.PNG';
    }
  }
}
