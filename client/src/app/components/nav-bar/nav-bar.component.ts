import { Component } from '@angular/core';
import {TranslateService} from '@ngx-translate/core';

interface Language{
  value: string;
  viewValue: string;
}

@Component({
  selector: 'nav-bar-component',
  templateUrl: './nav-bar.component.html',
  styleUrls: ['./nav-bar.component.css']
})
export class NavBarComponent {
  selectedLang: string;
  languages: Language[] = [
    {value: 'en', viewValue: 'EN'},
    {value: 'ru', viewValue: 'RU'}
  ]

  constructor(public translate: TranslateService) {
    translate.addLangs(['en', 'ru']);
    translate.setDefaultLang('en');

    const browserLang = translate.getBrowserLang();

    this.selectedLang = browserLang.match(/en|ru/) ? browserLang : 'en';
    translate.use(this.selectedLang);
  }

  changeLanguage() {
    this.translate.use(this.selectedLang);
  }
}