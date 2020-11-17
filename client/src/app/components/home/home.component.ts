import { Component } from '@angular/core';
import { FormControl } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { FileTypes } from 'src/app/common/global-constants'

@Component({
  selector: 'home-component',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {
  uploadFileMode: boolean = false;
  textIsProcessing: boolean = false;
  wrongFileExtension: boolean = false;

  fileControl: FormControl;
  fileToUpload: File = null;

  constructor(private http: HttpClient){
  }

  handleFileInput(files: FileList) {
    this.fileToUpload = files.item(0);
    const formData: FormData = new FormData();
    formData.append('file', this.fileToUpload, this.fileToUpload.name);

    if (this.fileToUpload.type != FileTypes.txt) {
      this.wrongFileExtension = true;
    }
    else {
      this.textIsProcessing = true;

      this.http.post('/api/uploadFile', formData)
        .subscribe(
          response => {
            this.textIsProcessing = false;
          console.log('success: ' + response);
        },
        response => {
          this.textIsProcessing = false;
          console.log('error: ' + response.error.message);
        }
        )
    }
    }
}