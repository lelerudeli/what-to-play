import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HeaderComponent } from '../shared/header/header.component';
import { HomePageComponent } from './home-page/home-page.component';
import { BaralhoComponent } from './home-page/baralho/baralho.component';
import { ConversaComponent } from './home-page/conversa/conversa.component';
import { PapelComponent } from './home-page/papel/papel.component';

const routes: Routes = [
  {
    path: '',
    children: [
      {
        path: 'header',
        component: HeaderComponent,
      },
      {
        path: 'home-page',
        component: HomePageComponent,
        children: [
          {
            path: 'baralho',
            component: BaralhoComponent
          },
          {
            path: 'conversa',
            component: ConversaComponent
          },
          {
            path: 'papel',
            component: PapelComponent
          }
        ]
      }
     
    ]
  },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class CoreRoutingModule { }