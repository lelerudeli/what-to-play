import { Component } from '@angular/core';
import { Profile } from '../../shared/models/user.model';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrl: './profile.component.css'
})
export class ProfileComponent {

  users: Profile[] = [
    {
      username: 'joao_games',
      nome: 'João Silva',
    },

  ];
}
