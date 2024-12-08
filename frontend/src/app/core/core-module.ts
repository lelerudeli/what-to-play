import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CoreRoutingModule } from './core-routing.module';
import { HomePageComponent } from './home-page/home-page.component';
import { BaralhoComponent } from './home-page/baralho/baralho.component';
import { ConversaComponent } from './home-page/conversa/conversa.component';
import { PapelComponent } from './home-page/papel/papel.component';

@NgModule({
  declarations: [
    HomePageComponent,
    BaralhoComponent,
    ConversaComponent,
    PapelComponent
  ],
  imports: [
    CoreRoutingModule,
    CommonModule
  ],
  providers: [],
  bootstrap: []
})
export class CoreModule { }