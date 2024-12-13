import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HeaderComponent } from './header/header.component';
import { HomePageComponent } from './selector/home-page/home-page.component';
import { SelectorComponent } from './selector/selector.component';
import { CorpoDinamicoComponent } from './selector/home-page/corpo-dinamico/corpo-dinamico.component';

const routes: Routes = [
  {
    path: '',
    children: [
      {
        path: 'selector',
        component: SelectorComponent,
        children: [
          {
            path: 'home-page',
            component: HomePageComponent,
            children: [
              {
                path: 'baralho',
                component: HomePageComponent
              }
            ]
          },
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