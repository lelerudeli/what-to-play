import { Component } from '@angular/core';
import { PythonService } from '../../shared/services/python.service';
import { Profile } from '../../shared/models/perfil.model';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrl: './profile.component.css'
})
export class ProfileComponent {

  users = [
    {
      username: 'Joao_games',
      nome: 'João',
      jogos: 6,
      amigos: 15
    }
  ];

  games = [
    { name: 'PIFE', description: 'até 8 jogadores • individual' },
    { name: 'TRUCO PAULISTA', description: '4 jogadores • em dupla' },
    { name: 'POKER', description: 'até 10 jogadores • individual' }
  ];

  constructor(
    private service: PythonService
  ){}

  ngOnInit(): void {
    this.service.perfil().subscribe({
      next: (perfil) => {
        console.log('Perfil:', perfil);
      },
      error: (err) => {
        console.error('Erro ao carregar perfil:', err);
      }
    });
  }
}
