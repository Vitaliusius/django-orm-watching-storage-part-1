import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard

def main():
    full = Passcard.objects.all()
    owner_name = full[0]
    active_passcards = Passcard.objects.filter(is_active=True)
    
    print('Всего пропусков: ', Passcard.objects.count(), '\nАктивных пропусков: ', len(active_passcards))


if __name__ == '__main__':
    main()