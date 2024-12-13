import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatIconModule } from '@angular/material/icon';
import { CardsComponent } from './cards/cards.component';

@NgModule({
  declarations: [
    CardsComponent,
   
  ],
  imports: [
    CommonModule,
    MatIconModule
  ],
  exports: [
    CardsComponent
  ],
  providers: [],
  bootstrap: []
})
export class SharedModule { }