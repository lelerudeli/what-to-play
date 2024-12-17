import { CommonModule } from "@angular/common";
import { NgModule } from "@angular/core";
import { ProfileComponent } from "./profile.component";
import { SharedModule } from "../../shared/shared.module";


@NgModule({
  declarations: [
    ProfileComponent
  ],
  imports: [
    SharedModule,
    CommonModule,
  ],
  providers: [],
  bootstrap: []
})
export class ProfileModule { }