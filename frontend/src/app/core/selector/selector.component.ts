import { Component } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-selector',
  templateUrl: './selector.component.html',
  styleUrl: './selector.component.css'
})
export class SelectorComponent {

  constructor(private router: Router) {}

  navigateTo(page: string): void {
    this.router.navigate([page], { queryParams: { source: 'homepage' } });
  }
   
}
