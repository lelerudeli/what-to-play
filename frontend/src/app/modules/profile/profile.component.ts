import { Component } from '@angular/core';
import { PythonService } from '../../shared/services/python.service';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrl: './profile.component.css'
})
export class ProfileComponent {

  constructor(
    private service: PythonService
  ){}

  ngOnInit(): void {
    this.service.perfil();

    console.log(this.service.perfil());
  }

}
