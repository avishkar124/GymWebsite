from django.shortcuts import render, redirect, get_object_or_404
from .models import Member


def add_member(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        age = request.POST.get("age")
        program = request.POST.get("program")

        Member.objects.create(
            name=name, email=email, phone=phone, age=age, program=program
        )

        return redirect("member_list")

    return render(request, "add_member.html")


def member_list(request):

    members = Member.objects.all()

    return render(request, "member_list.html", {"members": members})


def update_member(request, id):

    member = get_object_or_404(Member, id=id)

    if request.method == "POST":

        member.name = request.POST.get("name")
        member.email = request.POST.get("email")
        member.phone = request.POST.get("phone")
        member.age = request.POST.get("age")
        member.program = request.POST.get("program")

        member.save()

        return redirect("member_list")

    return render(request, "update_member.html", {"member": member})


def delete_member(request, id):

    member = get_object_or_404(Member, id=id)

    if request.method == "POST":

        member.delete()

        return redirect("member_list")

    return render(request, "delete_member.html", {"member": member})
