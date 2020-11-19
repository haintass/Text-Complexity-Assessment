import { Component } from '@angular/core';

@Component({
  selector: 'home-component',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {
  uploadFileMode: boolean = false;
  textIsProcessing: boolean = false;

  constructor(){ }

  onTextProcessing(textIsProcessing:boolean){
    this.textIsProcessing = textIsProcessing;
  }
}