import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { GameRegisterComponent } from './game-register.component';


const routes: Routes = [
  {
    path: '',
    component: GameRegisterComponent
  },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class GameRegisterRoutingModule { }