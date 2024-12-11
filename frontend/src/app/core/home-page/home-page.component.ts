import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-home-page',
  templateUrl: './home-page.component.html',
  styleUrl: './home-page.component.css'
})
export class HomePageComponent {

  activatedrouterRef: ActivatedRoute;

  constructor(
    private activatedRoute: ActivatedRoute
  ){
    this.activatedrouterRef = this.activatedRoute
  }

}
