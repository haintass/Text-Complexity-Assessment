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
  textAssessmentResult: any = {};
  tipForUser: string = null;

  constructor(){ }

  chooseInputMode(isUploadFileMode:boolean){
    this.uploadFileMode = isUploadFileMode;
    this.resetResult();
  }

  resetResult() {
    this.showAssessmentResult = false;
    this.textAssessmentResult = {};
    this.tipForUser = null;
  }

  onProcessingComplete(result:any){
    this.showAssessmentResult = true;
    this.textIsProcessing = false;
    this.textAssessmentResult = result;

    if (result.totalRating <= 40) {
      this.tipForUser = 'common.englishLevels.fluent'
    }
    else if (result.totalRating <= 60) {
      this.tipForUser = 'common.englishLevels.intermediate'
    }
    else {
      this.tipForUser = 'common.englishLevels.elementary'
    }
  }

  onTextProcessing(textIsProcessing:boolean){
    this.textIsProcessing = textIsProcessing;
  }
}