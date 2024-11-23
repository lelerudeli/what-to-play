import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HeaderComponent } from './header/header.component';
import { CoreRoutingModule } from './core-routing.modules';

@NgModule({
  declarations: [],
  imports: [
    CoreRoutingModule,
    CommonModule,
    HeaderComponent
  ],
  providers: [],
  bootstrap: []
})
export class CoreModule { }