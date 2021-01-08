import { Component } from '@angular/core';

@Component({
  selector: 'home-component',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {
  uploadFileMode: boolean = false;
  textIsProcessing: boolean = false;

  showAssessmentResult: boolean = false;
  textAssessmentResult: Number = 0;

  constructor(){ }

  chooseInputMode(isUploadFileMode:boolean){
    this.uploadFileMode = isUploadFileMode;
    this.resetResult();
  }

  resetResult() {
    this.showAssessmentResult = false;
    this.textAssessmentResult = 0;
  }

  onProcessingComplete(result:any){
    this.showAssessmentResult = true;
    this.textIsProcessing = false;
    this.textAssessmentResult = result.totalRating;
  }

  onTextProcessing(textIsProcessing:boolean){
    this.textIsProcessing = textIsProcessing;
  }
}