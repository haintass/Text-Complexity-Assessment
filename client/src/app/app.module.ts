import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { FormsModule }   from '@angular/forms';
import { HttpClient, HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';

/* CUSTOM COMPONENTS - BEGINS */
import { AppComponent } from './app.component';
import { AboutComponent } from './components/about/about.component';
import { ContactsComponent } from './components/contacts/contacts.component';
import { BackGroundComponent } from './components/background/background.component';
import { HomeComponent } from './components/home/home.component';
import { NavBarComponent } from './components/nav-bar/nav-bar.component';
import { AlertComponent } from './components/alert/alert.component';
import { FileUploadComponent } from './components/file-upload/file-upload.component';
import { TextInputComponent } from './components/text-input/text-input.component';
/* CUSTOM COMPONENTS - ENDS */

import { MaterialModule } from './modules/material.module';

/* TRANSLATE MODULES - BEGINS */
import {TranslateModule, TranslateLoader} from '@ngx-translate/core';
import {TranslateHttpLoader} from '@ngx-translate/http-loader';
/* TRANSLATE MODULES - ENDS */

// AoT requires an exported function for factories
export function HttpLoaderFactory(httpClient: HttpClient) {
  return new TranslateHttpLoader(httpClient);
}

@NgModule({
  declarations: [
    AppComponent,
    AboutComponent,
    ContactsComponent,
    BackGroundComponent,
    HomeComponent,
    NavBarComponent,
    AlertComponent,
    FileUploadComponent,
    TextInputComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    BrowserAnimationsModule,
    MaterialModule,
    FormsModule,
    TranslateModule.forRoot({
      loader: {
        provide: TranslateLoader,
        useFactory: HttpLoaderFactory,
        deps: [HttpClient]
      }
    })
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
