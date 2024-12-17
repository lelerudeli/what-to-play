import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatIconModule } from '@angular/material/icon';
import { HeaderComponent } from './header/header.component';
import { CardsComponent } from './cards/cards.component';
import { NavigationComponent } from './navigation/navigation.component';

@NgModule({
  declarations: [
    HeaderComponent,
    CardsComponent,
    NavigationComponent
  ],
  imports: [
    CommonModule,
    MatIconModule
  ],
  exports: [
    HeaderComponent,
    NavigationComponent,
    CardsComponent
  ],
  providers: [],
  bootstrap: []
})
export class SharedModule { }