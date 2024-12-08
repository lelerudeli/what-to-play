import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { NavigationComponent } from './navigation/navigation.component';
import { AppModule } from '../app.module';
import { MatIconModule } from '@angular/material/icon';
import { HeaderComponent } from './header/header.component';

@NgModule({
  declarations: [
    NavigationComponent,
    HeaderComponent
  ],
  imports: [
    CommonModule,
    MatIconModule
  ],
  exports: [
    NavigationComponent,
    HeaderComponent
  ],
  providers: [],
  bootstrap: []
})
export class SharedModule { }