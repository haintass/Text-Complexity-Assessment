import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';

/* CUSTOM COMPONENTS - BEGINS */
import { AppComponent } from './app.component';
import { AboutComponent } from './components/about/about.component';
import { BackGroundComponent } from './components/background/background.component';
import { HomeComponent } from './components/home/home.component';
import { NavBarComponent } from './components/nav-bar/nav-bar.component';
/* CUSTOM COMPONENTS - ENDS */

import { MaterialModule } from './modules/material.module';

@NgModule({
  declarations: [
    AppComponent,
    AboutComponent,
    BackGroundComponent,
    HomeComponent,
    NavBarComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    BrowserAnimationsModule,
    MaterialModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
