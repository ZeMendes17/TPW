import { Component, Input } from '@angular/core';
import { CommonModule, Location } from '@angular/common';
import {FormsModule, ReactiveFormsModule} from "@angular/forms";
import {Author} from "../author";
import {ActivatedRoute} from "@angular/router";
import {AUTHORS} from "../authorslist";

@Component({
  selector: 'app-author-details',
  standalone: true,
    imports: [CommonModule, ReactiveFormsModule, FormsModule],
  templateUrl: './author-details.component.html',
  styleUrl: './author-details.component.css'
})
export class AuthorDetailsComponent {
  @Input() author: Author | undefined = undefined;

  constructor(private route: ActivatedRoute, private location: Location) {
    this.getAuthor();
  }

  getAuthor(): void {
    let num: any = this.route.snapshot.paramMap.get('num');
    if (num != null)
      num = +num;
    else
      return;

    this.author = AUTHORS.find(author => author.num === num);
  }

  goBack(): void {
    this.location.back();
  }

  protected readonly undefined = undefined;
}
