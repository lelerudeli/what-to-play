import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CoreRoutingModule } from './core-routing.module';
import { HomePageComponent } from './selector/home-page/home-page.component';
import { SelectorComponent } from './selector/selector.component';
import { SharedModule } from '../shared/shared.module';
import { HeaderComponent } from './header/header.component';
import { NavigationComponent } from './navigation/navigation.component';
import { CorpoDinamicoComponent } from './selector/home-page/corpo-dinamico/corpo-dinamico.component';


@NgModule({
  declarations: [
    HomePageComponent,
    SelectorComponent,
    HeaderComponent,
    NavigationComponent,
    CorpoDinamicoComponent
  ],
  imports: [
    SharedModule,
    CoreRoutingModule,
    CommonModule
  ],
  providers: [],
  bootstrap: []
})
export class CoreModule { }