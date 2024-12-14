import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { NavigationComponent } from './navigation.component';
import { HomePageComponent } from '../home-page/home-page.component';

const routes: Routes = [
  {
    path: '',
    component: NavigationComponent
  },
  {
    path: 'home-page',
    component: HomePageComponent
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class NavigationRoutingModule { }