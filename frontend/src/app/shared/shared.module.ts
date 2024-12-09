import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { NavigationComponent } from './navigation/navigation.component';
import { AppModule } from '../app.module';
import { MatIconModule } from '@angular/material/icon';
import { HeaderComponent } from './header/header.component';
import { CardsComponent } from './cards/cards.component';

@NgModule({
  declarations: [
    NavigationComponent,
    HeaderComponent,
    CardsComponent
  ],
  imports: [
    CommonModule,
    MatIconModule
  ],
  exports: [
    NavigationComponent,
    HeaderComponent,
    CardsComponent
  ],
  providers: [],
  bootstrap: []
})
export class SharedModule { }